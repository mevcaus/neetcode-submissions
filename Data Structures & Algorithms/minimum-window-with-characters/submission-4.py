class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        unique_chars = len(t_count)
        found_chars = 0
        s_count = defaultdict(int)
        l,r = 0,0
        min_string = ""
        while r < len(s):
            char = s[r]
            if char in t_count:
                s_count[char] += 1
                if t_count[char] == s_count[char]:
                    found_chars +=1
                    while found_chars == unique_chars:
                        if min_string == "" or (r - l + 1) < len(min_string):
                            min_string = s[l:r + 1]
                        lchar = s[l]
                        if lchar in t_count:
                            s_count[lchar] -= 1
                            if s_count[lchar] < t_count[lchar]:
                                found_chars -= 1
                        l += 1
            r += 1
        return min_string
                        
                