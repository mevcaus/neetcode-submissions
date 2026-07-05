class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        for c in t:
            count[c] += 1
        goal_chars = len(count)
        have_chars, l, r = 0,0,0
        s_count = defaultdict(int)
        min_string = ""
        while r < len(s):
            s_count[s[r]] += 1
            if s_count[s[r]] == count[s[r]]:
                have_chars += 1
            while have_chars == goal_chars:
                if min_string == "" or len(min_string) > len(s[l:r + 1]):
                    min_string = s[l:r+1]
                s_count[s[l]] -= 1
                if s_count[s[l]] < count[s[l]]:
                    have_chars -= 1
                l += 1 
            r += 1
        return min_string

