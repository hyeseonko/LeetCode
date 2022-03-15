from itertools import chain

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest_candidates = [path[1] for path in paths]
        all_cities = list(chain.from_iterable(paths))
        for dest in dest_candidates:
            if all_cities.count(dest)==1:
                return dest