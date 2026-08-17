#!/usr/bin/env python3
"""Regenerate the counts and the solution index in README.md, plus stats.json.

Two directory generations coexist here: an older slug-only layout (`binary-search`)
and the current numbered one (`704-binary-search`), sometimes for the same problem,
and sometimes zero-padded (`0070-` vs `70-`). Counting directories therefore
overstates the total. The problem number is read from the statement instead, and
directories that resolve to the same number are merged into one entry.

stats.json exists so anything else that wants the count -- a profile README, a
dashboard -- reads it from the repository that can actually compute it, rather
than re-deriving it from paths and getting a different answer.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
STATS_JSON = ROOT / "stats.json"

SKIP_DIRS = {".git", ".github", "scripts"}
# The statement's title heading, with or without the LeetCode anchor -- the older
# sync wrote a bare <h2>704. Binary Search</h2>, the current one wraps it in <a>.
TITLE = re.compile(r"<h2>(?:<a href=\"([^\"]+)\">)?\s*(\d+)\.\s*(.+?)(?:</a>)?</h2>", re.S)
DIFFICULTY = re.compile(r"<h3>(Easy|Medium|Hard)</h3>")
# Tolerates zero padding so `0070-` and `70-` resolve alike.
DIR_NUMBER = re.compile(r"^0*(\d+)-(.+)$")

LANGUAGES = {".py": "Python", ".sql": "SQL", ".cpp": "C++", ".java": "Java", ".js": "JavaScript"}
DIFFICULTY_ORDER = ["Easy", "Medium", "Hard"]


@dataclass
class Problem:
    number: int
    title: str
    url: str
    difficulty: str = "—"
    solutions: list[Path] = field(default_factory=list)
    notes: list[Path] = field(default_factory=list)

    def languages(self) -> list[str]:
        return sorted({LANGUAGES.get(path.suffix, path.suffix.lstrip(".")) for path in self.solutions})


def _has_notes(path: Path) -> bool:
    """True when NOTES.md holds more than the zero-width space the sync seeds."""
    try:
        return bool(path.read_text().replace("​", "").strip())
    except OSError:
        return False


def scan() -> list[Problem]:
    problems: dict[int, Problem] = {}
    unresolved: list[str] = []

    for directory in sorted(ROOT.iterdir()):
        if not directory.is_dir() or directory.name in SKIP_DIRS:
            continue

        statement = directory / "README.md"
        text = statement.read_text() if statement.exists() else ""
        title_match = TITLE.search(text)
        dir_match = DIR_NUMBER.match(directory.name)

        if title_match:
            number = int(title_match.group(2))
            title = title_match.group(3).strip()
            url = title_match.group(1) or f"https://leetcode.com/problems/{directory.name}/"
        elif dir_match:
            number = int(dir_match.group(1))
            title = dir_match.group(2).replace("-", " ").title()
            url = f"https://leetcode.com/problems/{dir_match.group(2)}/"
        else:
            unresolved.append(directory.name)
            continue

        difficulty_match = DIFFICULTY.search(text)
        problem = problems.setdefault(number, Problem(number, title, url))
        if difficulty_match:
            problem.difficulty = difficulty_match.group(1)
        problem.solutions += [
            path
            for path in sorted(directory.iterdir())
            if path.is_file() and path.name not in ("README.md", "NOTES.md")
        ]
        if _has_notes(directory / "NOTES.md"):
            problem.notes.append(directory / "NOTES.md")

    for name in unresolved:
        print(f"note: could not resolve a problem number for {name}", file=sys.stderr)

    solved = [problem for problem in problems.values() if problem.solutions]
    for problem in problems.values():
        if not problem.solutions:
            # Statement synced, never finished. Counting it as solved would be a lie.
            print(f"note: #{problem.number} has no solution, excluded", file=sys.stderr)
    return sorted(solved, key=lambda problem: problem.number)


def tally(problems: list[Problem]) -> dict:
    by_language: dict[str, int] = {}
    for problem in problems:
        for language in problem.languages():
            by_language[language] = by_language.get(language, 0) + 1
    by_difficulty = {
        level: sum(1 for problem in problems if problem.difficulty == level)
        for level in DIFFICULTY_ORDER
    }
    return {
        "solved": len(problems),
        "by_language": dict(sorted(by_language.items(), key=lambda kv: -kv[1])),
        "by_difficulty": {k: v for k, v in by_difficulty.items() if v},
    }


def stats_block(stats: dict) -> str:
    languages = " · ".join(f"{count} {name}" for name, count in stats["by_language"].items())
    difficulties = " · ".join(f"{level} {count}" for level, count in stats["by_difficulty"].items())
    return f"**{stats['solved']} problems solved** — {languages}\n\n{difficulties}"


def index_block(problems: list[Problem]) -> str:
    lines = [
        "<details>",
        f"<summary>All {len(problems)} problems</summary>",
        "",
        "| # | Problem | Difficulty | Solution | Notes |",
        "| --- | --- | --- | --- | --- |",
    ]
    for problem in problems:
        solutions = ", ".join(
            f"[{LANGUAGES.get(path.suffix, path.suffix.lstrip('.'))}]"
            f"({path.parent.name}/{path.name})"
            for path in problem.solutions
        )
        notes = ", ".join(f"[notes]({path.parent.name}/{path.name})" for path in problem.notes)
        lines.append(
            f"| {problem.number} | [{problem.title}]({problem.url}) "
            f"| {problem.difficulty} | {solutions} | {notes} |"
        )
    lines += ["", "</details>"]
    return "\n".join(lines)


def replace(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:START -->)(.*?)(<!-- {name}:END -->)", re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"README.md is missing the {name} markers")
    return pattern.sub(lambda match: f"{match.group(1)}\n{body}\n{match.group(3)}", text)


def main() -> None:
    problems = scan()
    stats = tally(problems)

    text = README.read_text()
    text = replace(text, "STATS", stats_block(stats))
    text = replace(text, "INDEX", index_block(problems))
    README.write_text(text)
    STATS_JSON.write_text(json.dumps(stats, indent=2) + "\n")

    print(f"indexed {stats['solved']} problems: {stats['by_language']} {stats['by_difficulty']}")


if __name__ == "__main__":
    main()
