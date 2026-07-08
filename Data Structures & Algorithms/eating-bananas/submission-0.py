class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        k = r
        while l <= r:
            halfway = (r + l) // 2
            time_to_eat = 0
            for pile in piles:
                time_to_eat += math.ceil(pile / halfway)
            if time_to_eat <= h:
                k = min(k, halfway)
                r = halfway - 1
            else:
                l = halfway + 1
        return k
            # if koko can eat all the bananas
            # k = min(k, halfway)
            # shift r = l - 1
            # else return k