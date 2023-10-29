class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        list_word = s.split()
        return len(list_word[-1])