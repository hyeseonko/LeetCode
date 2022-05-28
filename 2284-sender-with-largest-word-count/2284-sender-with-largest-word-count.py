class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        conversation=dict()
        for message, sender in zip(messages, senders):
            if sender not in conversation:
                conversation[sender]=0
            conversation[sender]+=len(message.split(" "))
        sorted_conversation = sorted(conversation.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return sorted_conversation[0][0]