def patternToTokens(p):
    tokens = []
    for i, letter in enumerate(p):
        if i == len(p)-1 and letter != '*':
            tokens.append((letter, False))
        else:
            if letter != '*':
                tokens.append((letter, True if p[i+1]=='*' else False))
    return tokens

def check(s, t):
    if t == '.': return True
    return t==s

def matches(s, tokens):
    if not s: # if string is empty
        for t in tokens:
            if not t[1]:
                return False # if we have a non star token we lose
        return True # we win
    if not tokens: # if we have no tokens (and our string is not empty) we lose
        return False
    if not tokens[0][1]: # if we are looking at a non star token
        if check(s[0], tokens[0][0]): # check if the token matches the string
            return matches(s[1:], tokens[1:]) # cancel out
        else:
            return False
    else: # we have a starred token
        if check(s[0], tokens[0][0]):
            return matches(s[1:], tokens) or matches(s, tokens[1:])
        else:
            return matches(s, tokens[1:])


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tokens = patternToTokens(p)
        return matches(s, tokens)
