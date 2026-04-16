class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letter_count = Counter(tasks) # "{"A":3, .. }"  
        from collections import deque
        import heapq

        queue = deque() # (freq, next_avaliable_time)
        heap = [-letter_count[letter] for letter in letter_count] # Max heap of counts
        heapq.heapify(heap)

        time = 0
        while heap or queue:
            time += 1
            if heap:
                count = 1 + heapq.heappop(heap)
                if count < 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:  
                count = queue.popleft()[0]
                if count < 0:
                    heapq.heappush(heap, count)
            print("Time:", time, heap, queue)
        return time