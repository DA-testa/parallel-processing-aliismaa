# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)
    return output

    for i in range(m):
          job_time = times[i]

    start_time, thread_id = heapq.heappop(threads)

    print(thread_id, start_time)

    start_time += job_time

    heapq.heappush(threads, (start_time, thread_id))

    return output

def main():
 # n - thread count 
 # m - job count
    inp=input().split()
    n = int(inp[0])
    m = int(inp[1])

    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)

    


if __name__ == "__main__":
    main()
