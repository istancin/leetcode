import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        pattern = re.compile('[\W_]+')
        pattern = pattern.sub('', s.lower())
        
        half = int(len(pattern)/2) + 1
        if pattern[:half] == pattern[-1:-(half+1):-1]:
            return True
        return False