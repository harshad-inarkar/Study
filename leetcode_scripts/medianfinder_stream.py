#
import heapq

class MedianFinder:
    def __init__(self):
        # Max heap for the lower half
        self.left_heap = []
        # Min heap for the upper half
        self.right_heap = []

    def addNum1(self, num: int) -> None:
        # Push to max heap (invert num for max heap)
        heapq.heappush(self.left_heap, -num)
        # Balance: move largest of left_heap to right_heap

        if self.right_heap and -self.left_heap[0] > self.right_heap[0]:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))

        if len(self.left_heap) > len(self.right_heap)+1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        # Maintain size property
        if len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))


    def addNum(self,num):
        if len(self.left_heap) == len(self.right_heap):
            heapq.heappush(self.left_heap, -heapq.heappushpop(self.right_heap,num))
        else:
            heapq.heappush(self.right_heap, -heapq.heappushpop(self.left_heap,-num))



    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2




# Unit tests
def test_MedianFinder():
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2
    mf.addNum(4)
    assert mf.findMedian() == 2.5
    mf.addNum(5)
    assert mf.findMedian() == 3

    # Test with negative numbers
    mf2 = MedianFinder()
    for n in [-1, -2, -3, -4, -5]:
        mf2.addNum(n)
    assert mf2.findMedian() == -3

    # Test with duplicates
    mf3 = MedianFinder()
    for n in [2, 2, 2, 2]:
        mf3.addNum(n)
    assert mf3.findMedian() == 2

    # Test with single element
    mf4 = MedianFinder()
    mf4.addNum(42)
    assert mf4.findMedian() == 42

    print("All test cases passed!")

test_MedianFinder()
