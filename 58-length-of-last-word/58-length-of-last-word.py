class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return False
        s = s.strip()
        return len(s.split(' ')[-1])