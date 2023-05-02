class WeightedGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edges(self, v1, v2, weight):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append((v2, weight))
            self.adj_list[v2].append((v1, weight))
            return True
        return False

    def remove_edge(self, v1, v2):
        # check if v1 and v2 exist in the adjacency list
        if v1 in self.adj_list and v2 in self.adj_list:
            # create a new adjacency list for vertex v1 without the edge to vertex v2
            new_adj_list_v1 = []
            for vertex, weight in self.adj_list[v1]:
                if vertex != v2:  # exclude vertex v2
                    new_adj_list_v1.append((vertex, weight))
            self.adj_list[v1] = new_adj_list_v1  # update adjacency list for v1

            # create a new adjacency list for vertex v2 without the edge to vertex v1
            new_adj_list_v2 = []
            for vertex, weight in self.adj_list[v2]:
                if vertex != v1:  # exclude vertex v1
                    new_adj_list_v2.append((vertex, weight))
            self.adj_list[v2] = new_adj_list_v2  # update adjacency list for v2

            return True
        return False

    def remove_vertex(self, v):
        # Check if vertex v exists in the graph
        if v in self.adj_list:
            # Remove vertex v from the graph
            del self.adj_list[v]
            # For each remaining vertex in the graph
            for vertex in self.adj_list:
                # Remove all edges that connect to vertex v
                new_adj_list = []
                for v2, weight in self.adj_list[vertex]:
                    if v2 != v:
                        new_adj_list.append((v2, weight))
                self.adj_list[vertex] = new_adj_list

    def dfs(self, start, visited=None):
        if visited == None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for key_node, weight in self.adj_list[start]:
            if key_node not in visited:
                self.dfs(key_node, visited)

    def bfs(self, start):
        visited = {}
        que = []
        result = []

        visited[start] = True
        que.append(start)

        while len(que) > 0:
            current = que.pop(0)
            result.append(current)
            neighbours = self.adj_list[current]

            for item, weight in neighbours:
                if item not in visited.keys():
                    visited[item] = True
                    que.append(item)
        return result

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


graph = WeightedGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edges("A", "B", 15)
graph.add_edges("A", "C", 12)
graph.add_edges("A", "D", 4)
graph.add_edges("B", "D", 7)
graph.add_edges("C", "E", 41)

graph.print_graph()

print()
graph.remove_vertex("C")
print("After removing vertex:-")
graph.print_graph()

print()
graph.remove_edge("A", "D")
print("After removing a edge:-")
graph.print_graph()

print("\nDFS Traversal :-")
graph.dfs("A")

print()
print("\nBFS Traversal :-")
print(graph.bfs("A"))