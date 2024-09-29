class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        hFences.sort()
        vFences.sort()
        h_diff = set()
        v_diff = set()
        for i in range(1, len(hFences)):
            h_diff.add(hFences[i] - hFences[i - 1])
        for i in range(1, len(vFences)):
            v_diff.add(vFences[i] - vFences[i - 1])
        max_len = 0
        for h in h_diff:
            if h in v_diff:
                max_len = max(max_len, h)
        return max_len * max_len % (10**9 + 7) if max_len > 0 else -1
