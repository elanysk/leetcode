class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        for i, letter in enumerate(strs[0]):
            for word in strs: 
                if i == len(word) or word[i] != letter: return out
            out += letter
        return out
