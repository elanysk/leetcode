class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(5, (n+1)//2, pow(10,9) + 7) * pow(4, n//2, pow(10,9) + 7) % (pow(10,9) + 7)
