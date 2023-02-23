class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneHeap = [-i for i in stones]
        heapq.heapify(stoneHeap)

        while len(stoneHeap) > 1:
            stoneOne = heapq.heappop(stoneHeap)
            stoneTwo = heapq.heappop(stoneHeap)
            if stoneTwo > stoneOne:
                heapq.heappush(stoneHeap, stoneOne - stoneTwo)

        stoneHeap.append(0)
        return -(stoneHeap[0]) 