class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c] += 1
        s2_freq = defaultdict(int)
        l = 0
        r = 0
        while r < len(s2):
            s2_freq[s2[r]] += 1
            while s2_freq[s2[r]] > s1_freq[s2[r]]:
                s2_freq[s2[l]] -= 1
                l += 1
            r += 1
            if s1_freq == s2_freq:
                return True
        return False