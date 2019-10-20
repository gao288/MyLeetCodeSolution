import heapq
import math
class Solution:
    def kClosest(self, points, K):
        def _heappush_max(heap, item):
            heap.append(item)
            heapq._siftdown_max(heap, 0, len(heap)-1)
        heap = []
        heapq._heapify_max(heap) 
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            _heappush_max(heap,(distance,point))
            if len(heap) > K:
                heapq._heappop_max(heap)
                
        
        return [x[1] for x in heap]

s = Solution()
print(s.kClosest([[1,3],[-2,2]],1))