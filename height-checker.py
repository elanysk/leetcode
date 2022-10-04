class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        s = [0]*101
        for h in heights:
            s[h] += 1
        i=0
        for index, e in enumerate(s):
            for j in range(e):
                if heights[i] != index:
                    count+=1
                i+=1
        return count
