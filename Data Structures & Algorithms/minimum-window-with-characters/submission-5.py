class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        unique_chars = len(t_count)
        found_chars = 0
        s_count = defaultdict(int)
        l,r = 0,0
        min_l = -1
        min_r = -1
        while r < len(s):
            char = s[r]
            if char in t_count:
                s_count[char] += 1
                if t_count[char] == s_count[char]:
                    found_chars +=1
                    while found_chars == unique_chars:
                        if min_l == -1 or min_r - min_l > r - l:
                            min_l = l
                            min_r = r
                        lchar = s[l]
                        if lchar in t_count:
                            s_count[lchar] -= 1
                            if s_count[lchar] < t_count[lchar]:
                                found_chars -= 1
                        l += 1
            r += 1
        return "" if min_l == - 1 else s[min_l:min_r + 1]
                        
                