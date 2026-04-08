class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #brute force
        elem_freq = {}
        for num in nums:
            elem_freq[num] = elem_freq.get(num, 0)+1

        res = []
        for num, count in elem_freq.items():
            if count > len(nums)//3:
                res.append(num)
        
        return res


        