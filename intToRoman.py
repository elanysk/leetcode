# Given an integer, convert it to a roman numeral.

def intToRoman(num, s=""):
    if num>=1000: return intToRoman(num-1000, s+"M")
    if num>=900: return intToRoman(num-900, s+"CM")
    if num>=500: return intToRoman(num-500, s+"D")
    if num>=400: return intToRoman(num-400, s+"CD")
    if num>=100: return intToRoman(num-100, s+"C")
    if num>=90: return intToRoman(num-90, s+"XC")
    if num>=50: return intToRoman(num-50, s+"L")
    if num>=40: return intToRoman(num-40, s+"XL")
    if num>=10: return intToRoman(num-10, s+"X")
    if num>=9: return intToRoman(num-9, s+"IX")
    if num>=5: return intToRoman(num-5, s+"V")
    if num>=4: return intToRoman(num-4, s+"IV")
    return s + "I"*num