class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        for c in s1:
            freq[c] += 1
        count = defaultdict(int)
        l = 0
        r = 0
        while r < len(s2):
            if count == freq:
                return True
            if s2[r] in freq:
                count[s2[r]] += 1
                while count[s2[r]] > freq[s2[r]]:
                    count[s2[l]] -= 1
                    l += 1
                r += 1
            else:
                l = r + 1
                r = l
                count.clear()
        if count == freq:
            return True
        return False