class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        current_blocker = float('-inf')
        car_fleets = 0
        for p,s in cars[::-1]:
            finish_time = (target - p) / s
            if finish_time > current_blocker:
                car_fleets += 1
                current_blocker = finish_time
        return car_fleets
