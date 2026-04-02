class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #brute force
        # uniqueElemCount = {}

        # for i in range(len(nums)):
        #     if nums[i] not in uniqueElemCount:
        #         uniqueElemCount[nums[i]] = 0
        #     uniqueElemCount[nums[i]] += 1

        # for key, value in uniqueElemCount.items():
        #     if value > len(nums)/2 :
        #         return key

        #optimized O(1) space complexity O(n) TC
        #boyer-moore voting algo remove - if something appear more than n/2 times 
        #then it will still exist in the end

        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
