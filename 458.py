
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        T = minutesToTest // minutesToDie
        T+=1
        x = 0
        while (T)**x < buckets:
            x = x+1
        return x
