class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        unique_chars = len(t_count)
        l,r = 0, 0
        min_l = min_r = -1
        s_count = defaultdict(int)
        found_chars = 0
        while r < len(s):
            if s[r] in t_count:
                s_count[s[r]] += 1
                if s_count[s[r]] == t_count[s[r]]:
                    found_chars += 1
                    while found_chars == unique_chars:
                        if min_l == -1 or min_r - min_l > r - l:
                            min_l,min_r = l,r
                        if s[l] in t_count:
                            s_count[s[l]] -= 1
                            if s_count[s[l]] < t_count[s[l]]:
                                found_chars -= 1
                        l += 1
            r += 1
        return "" if min_l == -1 else  s[min_l:min_r + 1]