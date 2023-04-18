class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        l = min(l1, l2)
        res = []
        for i in range(l):
            res.append(word1[i])
            res.append(word2[i])
        if l1>l2:
            res.append(word1[l:])
        elif l2>l1:
            res.append(word2[l:])
        return ''.join(res)