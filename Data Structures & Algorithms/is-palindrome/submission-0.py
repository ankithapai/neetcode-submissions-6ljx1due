class Solution:
    def isPalindrome(self, s: str) -> bool:
        pStr = ''

        for sch in s.lower():
            if sch.isalnum():
                pStr +=sch
        
        left = 0
        right = len(pStr) - 1

        while left < right:
            if pStr[left] != pStr[right]:
                return False
            else:
                left +=1
                right -=1
        
        return True
