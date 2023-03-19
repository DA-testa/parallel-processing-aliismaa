# python3
import heapq
# n - thread count 
# m - job count
# data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
n, m = map(int, input().split())
data = list(map(int, input().split()))


threads = [(0, i) for i in range(n)]

for i in range(m):

    job = data[i]

    start_time, thread_index = heapq.heappop(threads)
    
# TODO: print out the results, each pair in it's own line
    print(thread_index, start_time)

    start_time += job

    heapq.output(threads, (start_time, thread_index))
