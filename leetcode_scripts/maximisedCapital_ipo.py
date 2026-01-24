def findMaximizedCapital(k, w, profits, capital):
    """
    Leetcode 502. IPO
    Given the number of projects k, initial capital w, profits and capital arrays,
    return the maximized capital after at most k projects.
    """
    import heapq

    # Pair up capital and profit, and sort by capital required
    projects = sorted(zip(capital, profits))
    n = len(profits)
    max_profit_heap = []
    i = 0

    for _ in range(k):
        # Push all projects that can be afforded into max heap
        while i < n and projects[i][0] <= w:
            # Use negative profit for max heap
            heapq.heappush(max_profit_heap, -projects[i][1])
            i += 1
        if not max_profit_heap:
            break
        # Pop the most profitable project
        w += -heapq.heappop(max_profit_heap)
    return w

# Unit tests
import unittest

class TestFindMaximizedCapital(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(findMaximizedCapital(2, 0, [1,2,3], [0,1,1]), 4)
    def test_example2(self):
        self.assertEqual(findMaximizedCapital(3, 0, [1,2,3], [0,1,2]), 6)
    def test_no_projects(self):
        self.assertEqual(findMaximizedCapital(0, 100, [1,2,3], [0,1,2]), 100)
    def test_cannot_afford_any(self):
        self.assertEqual(findMaximizedCapital(2, 0, [1,2,3], [1,2,3]), 0)
    def test_all_zero_profits(self):
        self.assertEqual(findMaximizedCapital(3, 0, [0,0,0], [0,0,0]), 0)
    def test_large_k(self):
        self.assertEqual(findMaximizedCapital(10, 1, [2,3,5], [0,1,2]), 11)
    def test_duplicate_capital(self):
        self.assertEqual(findMaximizedCapital(2, 1, [2,2,3], [1,1,2]), 6)

if __name__ == "__main__":
    unittest.main()
