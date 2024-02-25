class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  

    def is_safe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def assign_colors(self):
        result = [-1] * self.V
        result[0] = 0

        for v in range(1, self.V):
            available = [True] * self.V

            for i in range(self.V):
                if self.graph[v][i] == 1 and result[i] != -1:
                    available[result[i]] = False

            c = 0
            while c < self.V:
                if available[c]:
                    break
                c += 1

            result[v] = c

        return result

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

colors = g.assign_colors()
print("Assigned colors to vertices:")
for v in range(g.V):
    print(f"Vertex {v}: Color {colors[v]}")
