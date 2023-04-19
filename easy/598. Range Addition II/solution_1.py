class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m_min, n_min = m, n
        for op in ops:
            m_min = min(m_min, op[0])
            n_min = min(n_min, op[1])
        return m_min * n_min