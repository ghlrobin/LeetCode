class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])

        def dijkstra(start):
            dist = [math.inf] * n
            ways = [0] * n
            heap = [(0, start)]
            dist[start] = 0
            ways[start] = 1
            while heap:
                d, u = heappop(heap)
                if dist[u] < d:
                    continue 
                for v, time in graph[u]:
                    if dist[v] > d + time:
                        dist[v] = d + time
                        ways[v] = ways[u]
                        heappush(heap, (dist[v], v))
                    elif dist[v] == d + time:
                        ways[v] = (ways[v] + ways[u]) % (10**9 + 7)
            return ways[n - 1]

        return dijkstra(0)