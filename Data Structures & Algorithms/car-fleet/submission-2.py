class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        current_blocker = 0
        sorted_cars = sorted(zip(position, speed), key=lambda p: p[0], reverse=True)
        for pos, sp in sorted_cars:
            finish_time = (target - pos) / sp
            if finish_time > current_blocker:
                current_blocker = finish_time
                res += 1
        return res