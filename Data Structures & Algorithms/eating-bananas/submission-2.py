class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        mes = r
        while l <= r:
            halfway = (l + r) // 2
            hours_to_eat = 0
            for pile in piles:
                hours_to_eat += math.ceil(pile / halfway)
            if hours_to_eat <= h:
                mes = halfway
                r = halfway - 1
            else:
                l = halfway +1
        return mes