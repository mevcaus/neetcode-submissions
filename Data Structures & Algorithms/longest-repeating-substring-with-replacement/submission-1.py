class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = defaultdict(int)
        max_freq = 0
        l = 0
        r = 0
        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(freq[s[r]], max_freq)
            while r - l + 1> max_freq + k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res