class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        current_blocker = 0
        spos = sorted(zip(position, speed), key=lambda p: p[0], reverse=True)
        for pos, spd in spos:
            finish_time = (target - pos) / spd
            if finish_time > current_blocker:
                current_blocker = finish_time
                res += 1
        return res