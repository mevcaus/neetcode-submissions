class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)
        min_string = ""
        l = 0
        r = 0
        r_freq = defaultdict(int)
        have = 0
        for c in t:
            t_freq[c] += 1
        needed_unique_chars = len(t_freq)
        while r < len(s):
            r_freq[s[r]] += 1
            if t_freq[s[r]] == r_freq[s[r]]:
                have += 1
            while have == needed_unique_chars:
                if min_string == "" or len(min_string) > len(s[l:r + 1]):
                    min_string = s[l:r+1]
                r_freq[s[l]] -= 1
                if r_freq[s[l]] < t_freq[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return min_string
