# Đọc số đỉnh và số cạnh
n, m = map(int, input().split())

# Tạo một danh sách để biểu diễn đồ thị
graph = {}
for i in range(1, n + 1):
    graph[i] = []

# Đọc các cạnh và thêm chúng vào danh sách đồ thị
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
# Tính số cạnh liền kề cho từng đỉnh
for node in graph:
    degree = len(graph[node])
    print( degree)
