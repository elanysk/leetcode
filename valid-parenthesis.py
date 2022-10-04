class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p1, p2, p3 = 0, 0, 0
        for c in s:
            if c=='(': p1+=1
            if c=='{': p2+=1
            if c=='[': p3+=1
            if c==')': p1-=1
            if c=='}': p2-=1
            if c==']': p3-=1
            if (p1<0 or p2<0 or p3<0): return False
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            if c==')':
                if stack.pop() != '(':
                    return False
            if c=='}':
                if stack.pop() != "{":
                    return False
            if c==']': 
                if stack.pop() != "[":
                    return False 
        return p1==0 and p2==0 and p3==0
