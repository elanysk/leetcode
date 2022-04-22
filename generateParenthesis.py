# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n, p=0):
    if p > 0 and n > 0:
        return [")" + x for x in generateParenthesis(n, p - 1)] + ["(" + x for x in generateParenthesis(n - 1, p + 1)]
    if p > 0:
        return [")" + x for x in generateParenthesis(n, p - 1)]
    if n > 0:
        return ["(" + x for x in generateParenthesis(n - 1, p + 1)]
    return [""]
