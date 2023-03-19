# python3
import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [(0,i) for i in range(n)]
    heapq.heapify(threads)
    return output

    for i, j in enamurate(data):
        time, job = heapq.heappop(threads)
        output.append((job, time))
        heapq.heappush(threads, (time + j, job))

    return output

def main():
 # n - thread count 
 # m - job count
    inp=input().split()
    n = int(inp[0])
    m = int(inp[1])

    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)

    for i in range(m):
        print(result[i][0],result[i][1])


if __name__ == "__main__":
    main()
