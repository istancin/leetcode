class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        if n==1: 
            if target[0]==1:
                return True
            else:
                return False
        h, s = [-x for x in target], sum(target)
        heapq.heapify(h)
        curr = heappop(h) * -1
        while curr!=1:
            s -= curr
            if s==1:
                return True
            if s>curr:
                return False
            num = curr%s
            if num<1:
                return False
            heappush(h, -num)
            s += num
            curr = heappop(h) * -1
        return True