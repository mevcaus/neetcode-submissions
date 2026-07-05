class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        heap = []
        res = []
        for i in range(k):
            q.append(nums[i])
            heapq.heappush(heap, -nums[i])
        r = k
        while r < len(nums):
            res.append(-heap[0])
            removed = q.popleft()
            heap.remove(-removed)
            heapq.heapify(heap)
            q.append(nums[r])
            heapq.heappush(heap, -nums[r])
            r += 1
        res.append(-heap[0])
        return res