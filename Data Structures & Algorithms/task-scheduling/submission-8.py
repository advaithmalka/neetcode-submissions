class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = defaultdict(int)
        maxCount = 0
        startingTask = ""
        for task in tasks:
            taskCount[task] += 1

        heap = taskCount.values()
        heap = [-value for value in heap]
        heapq.heapify(heap)

        cycles = 0
        cooldown = collections.deque()
        while heap or cooldown:
            cycles += 1
            if heap:
                task = -heapq.heappop(heap)
                task -= 1
                if task:
                    cooldown.append((task, cycles + n))
            if cooldown and cooldown[0][1] == cycles:
                value, _ = cooldown.popleft()
                heapq.heappush(heap, -value)
        return cycles
            
        


        
        
