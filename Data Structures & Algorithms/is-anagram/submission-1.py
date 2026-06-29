class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for c in s:
            s_hash[c] += 1
        for c in t:
            t_hash[c] += 1
        return s_hash == t_hash
        