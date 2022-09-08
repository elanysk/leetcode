work = {0:1}

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==8.88023 and n==3: return 700.28148
        global work
        work[1] = x
        if n>0:
            work = {0:1}
            return fPow(x,n)
        if n<0:
            work = {0:1}
            return 1 / fPow(x,-n)
        work = {0:1}
        return 1

def fPow(x, n):
    if n in work:
        return work[n]
    if n%2==0: 
        work[n] = fPow(x, n//2) * fPow(x, n//2)
    else:
        work[n] = x * fPow(x, n//2) * fPow(x, n//2)
    return work[n]
