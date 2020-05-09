class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqr=0
        i=1
        while(i*i<=num):
            sqr=i*i
            if sqr==num:
                return True
            i=i+1
        return False