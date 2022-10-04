class Solution:
    def generateParenthesis(self, n: int, p=0):
        if p > 0 and n > 0:
            return [")" + x for x in self.generateParenthesis(n, p - 1)] + ["(" + x for x in self.generateParenthesis(n - 1, p + 1)]
        if p > 0:
            return [")" + x for x in self.generateParenthesis(n, p - 1)]
        if n > 0:
            return ["(" + x for x in self.generateParenthesis(n - 1, p + 1)]
        return [""]
