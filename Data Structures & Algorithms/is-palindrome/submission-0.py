class Solution:
    def isPalindrome(self, s: str) -> bool:
        combine = ''.join(x.lower() for x in s.split(' '))
        left, right = 0, len(combine)-1
        while left<right:
            if not combine[left].isalnum():
                left +=1
                continue
            if not combine[right].isalnum():
                right-=1
                continue
            if combine[left] != combine [right]:
                return False
            left += 1
            right -=1
        return True      
        