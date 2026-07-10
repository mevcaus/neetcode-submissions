class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        mes = r
        while l <= r:
            halfway = (l + r) // 2
            hte = 0
            for pile in piles:
                hte += math.ceil(pile / halfway)
            if hte <= h:
                mes = min(mes, halfway)
                r = halfway - 1
            else:
                l = halfway + 1
        return mes