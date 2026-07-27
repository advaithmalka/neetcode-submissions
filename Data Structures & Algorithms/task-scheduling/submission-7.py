class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        taskCount = defaultdict(int)
        for task in tasks:
            taskCount[task] += 1
        
        q = collections.deque()
        values = taskCount.values()
        maxHeap = [-value for value in values]
        heapq.heapify(maxHeap)

        while maxHeap or q:
            res += 1
            if maxHeap:
                freq = -heapq.heappop(maxHeap)
                newFreq = freq - 1
                if newFreq != 0:
                    q.append((newFreq, res + n))
        
            if q and q[0][1] == res:
                freq, _ = q.popleft()
                heapq.heappush(maxHeap, -freq)
        return res