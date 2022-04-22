def romanToInt(s, out=0):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if len(s) == 0: return out
    if len(s) == 1: return values[s] + out
    if s[0:2] in {"IV","IX","XL","XC","CD","CM"}: return romanToInt(s[2:], out + values[s[1]] - values[s[0]])
    return romanToInt(s[1:], out + values[s[0]])