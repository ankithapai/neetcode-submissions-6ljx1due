class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}
        for num in nums:
            if num not in colors:
                colors[num] = 0
            colors[num] +=1
        
        ptr = 0
        countZero = colors.get(0, 0)
        while countZero > 0:
            nums[ptr] = 0
            ptr += 1
            countZero -= 1

        countOne = colors.get(1, 0)
        while countOne > 0:
            nums[ptr] = 1
            ptr += 1
            countOne -= 1
        
        countTwo = colors.get(2, 0)
        while countTwo > 0:
            nums[ptr] = 2
            ptr += 1
            countTwo -= 1
        