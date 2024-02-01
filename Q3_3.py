class Q3_3:
    def f3(self, a, start, end): 
        #a is the adjacency matrix representing the given graph
        # start is a starting point
        # end is a ending point
        shortest_path, path_length = self.dijkstra(a, start, end)
        print(f"Shortest path from {chr(start + 65)} to {chr(end + 65)}:")
        if shortest_path:
            print(" -> ".join(map(lambda vertex: chr(vertex + 65), shortest_path)))
            print(f"Total path length: {path_length}")
        else:
            print("No path exists.")

    def dijkstra(self, a, start, end):
        num_vertices = len(a)
        visited = [False] * num_vertices
        distances = [float('inf')] * num_vertices
        previous_vertices = [-1] * num_vertices

        distances[start] = 0

        for _ in range(num_vertices):
            min_distance = float('inf')
            current_vertex = -1

            for vertex in range(num_vertices):
                if not visited[vertex] and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    current_vertex = vertex
                    
            visited[current_vertex] = True

            for neighbor in range(num_vertices):
                if (
                    not visited[neighbor]
                    and a[current_vertex][neighbor] != 0
                    and distances[current_vertex] + a[current_vertex][neighbor] < distances[neighbor]
                ):
                    distances[neighbor] = distances[current_vertex] + a[current_vertex][neighbor]
                    previous_vertices[neighbor] = current_vertex

        # Build the path from start to end
        path = []
        current_vertex = end
        while previous_vertices[current_vertex] != -1:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]
        path.insert(0, start)

        return path, distances[end]
        pass
        