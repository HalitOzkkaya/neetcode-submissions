class Solution:
    def climbStairs(self, n: int) -> int:
        
        i = 0
        v1 = 0
        v2 = 1

        while i < n:
            temp = v1 + v2
            if v1 < v2:
                v1 = temp
            else:
                v2 = temp
            i += 1

        return max(v1,v2)
