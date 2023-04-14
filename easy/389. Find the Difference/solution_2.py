class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        res = ord(s[0]) ^ ord(t[0])
        for i in range(1, len(t)):
            if i==len(t)-1:
                res ^= ord(t[i])
            else:
                res ^= ord(t[i])
                res ^= ord(s[i])
        return chr(res)