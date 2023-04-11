class Solution:
    def removeStars(self, s: str) -> str:
        star = '*'
        while True:
            if star not in s:
                break
            star_index = s.index('*')
            cur_pos = star_index - 1
            s = s[:cur_pos] + s[star_index+1:]
        return s