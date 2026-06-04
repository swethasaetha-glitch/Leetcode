# Last updated: 6/4/2026, 9:42:11 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence))==26