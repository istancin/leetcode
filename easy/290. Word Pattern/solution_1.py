class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        pat_s = {}
        s_pat = set()
        for i, p in enumerate(pattern):
            if p in pat_s:
                if s[i] != pat_s[p]:
                    return False
            else:
                if s[i] in s_pat:
                    return False
                pat_s[p] = s[i]
                s_pat.add(s[i])
        return True