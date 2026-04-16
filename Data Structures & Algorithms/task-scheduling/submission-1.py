from _heapq import heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu_cycles = 0
        counts_of_letter = Counter(tasks) # {'A' : 3}
        heap = [-counts_of_letter[letter] for letter in counts_of_letter]
        import heapq
        from collections import deque

        heapq.heapify(heap) 
        queue = deque()

        time = 0 
        while heap or queue: 
            time += 1
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    queue.append((cnt, time + n))
            while queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time

        # import heapq
        # task_counts = Counter(tasks) 
        # unique_tasks = [ (0, k) for k in task_counts]
        # heapq.heapify(unique_tasks)

        # while unique_tasks:
        #     cooldown, task = heapq.heappop(unique_tasks)
        #     if task_counts[task] == 0: 
        #         task_counts.pop(task)
        #         continue
    
        #     if cooldown == 0:
        #         task_counts[task] -= 1
        #         heapq.heappush(unique_tasks, (-n, task))
        #         print("task reset with n:", -n, task)
        #     else:
        #         heapq.heappush(unique_tasks, (cooldown + 1, task))
        #         print("task cooldown:", cooldown+1, task)

        #     cpu_cycles += 1
        #     print("cpu:", cpu_cycles)

        # return cpu_cycles