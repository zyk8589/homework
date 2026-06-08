import heapq

class MedianFinder:
    def __init__(self):
        self.small = []   # 大顶堆
        self.large = []   # 小顶堆

    def addNum(self, num: int) -> None:
        # 先加入大顶堆
        heapq.heappush(self.small, -num)
        
        # 把大顶堆的最大值移到小顶堆
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # 保持 small 比 large 多一个或相等
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


# 测试代码
if __name__ == "__main__":
    mf = MedianFinder()
    
    mf.addNum(3)
    print(f"add 3, 中位数: {mf.findMedian()}")  # 3.0
    
    mf.addNum(1)
    print(f"add 1, 中位数: {mf.findMedian()}")  # 2.0
    
    mf.addNum(4)
    print(f"add 4, 中位数: {mf.findMedian()}")  # 3.0
    
    mf.addNum(1)
    print(f"add 1, 中位数: {mf.findMedian()}")  # 2.0
    
    mf.addNum(5)
    print(f"add 5, 中位数: {mf.findMedian()}")  # 3.0