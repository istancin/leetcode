from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #assert len(s)+1 == len(t)
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        for i in range(len(t)):
            if i==len(t)-1:
                count_t[t[i]] += 1
            else:
                count_t[t[i]] += 1
                count_s[s[i]] += 1
        for ch, count in count_t.items():
            if count_s[ch] != count:
                return ch