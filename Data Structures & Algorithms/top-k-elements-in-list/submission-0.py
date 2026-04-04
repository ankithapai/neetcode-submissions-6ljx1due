class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1

        my_heap = []
        
        for key, value in freq_map.items():
            heapq.heappush(my_heap, [value, key])
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        
        res = []
        while len(my_heap) > 0:
            count, num = heapq.heappop(my_heap)
            res.append(num)

        return res
