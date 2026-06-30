class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        heap = []
        res = []
        for num in nums:
            frequency[num] += 1
        for key, value in frequency.items():
            heapq.heappush(heap, [-value, key])
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        