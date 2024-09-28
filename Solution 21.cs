class Solution(object):
    def getResults(self, queries):
        results = []
        n = 50000
        tree = [0] * (2 * n)

        def update(p, value):
            p += n
            tree[p] = value
            while p > 1:
                tree[p >> 1] = max(tree[p], tree[p ^ 1])
                p >>= 1

        def query(l, r):
            l += n
            r += n
            res = 0
            while l < r:
                if l & 1:
                    res = max(res, tree[l])
                    l += 1
                if r & 1:
                    res = max(res, tree[r - 1])
                    r -= 1
                l >>= 1
                r >>= 1
            return res

        for q in queries:
            if q[0] == 1:
                update(q[1], q[1])
            else:
                res = query(0, q[1] + 1)
                results.append(res >= q[2])

        return results
