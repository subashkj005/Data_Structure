class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):

        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return
        return False

    def add_edges(self,v1,v2):
        # eg: if vertex A and B passed for edge connection
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            #  adj_list = {
            #              'A': ['B']
            #             }
            self.adj_list[v2].append(v1)
            #  adj_list = {
            #              'B': ['A']
            #             }
            return True
        return False

    def remove_edges(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            # Its for if the vertex have any edges with any other vertexes.
            # eg: if deleting 'D'
            #    {
            #      'A': ['B','C','D']
            #      'B': ['A','D']
            #      'C': ['A', 'D']
            #      'D': ['A','B','C']
            #    }
            # Through this loop delete connections with other vertexes(in A,B,C)
            for each_vertex in self.adj_list:
                if vertex in self.adj_list[each_vertex]:
                    self.adj_list[each_vertex].remove(vertex)
        # finally delete the vertex fully(D)
        del self.adj_list[vertex]


    def dfs(self, start, visited = None):
        if visited == None:
            visited = set()
            #In set, duplicates are not entered
        visited.add(start)
        print(start, end=" ")
        for key_node in self.adj_list[start]:
            if key_node not in visited:
                self.dfs(key_node, visited)

    def bfs(self, start):
        visited = {}
        que = []
        result = []

        visited[start] = True
        que.append(start)

        while len(que)>0:
            current = que.pop(0)
            result.append(current)
            neighbours = self.adj_list[current]

            for item in neighbours:
                if item not in visited.keys():
                    visited[item] = True
                    que.append(item)
        return result

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])

    def has_path_dfs(self, u, v):
        visited = set()
        self.dfs(u, visited)
        if v in visited:
            return True
        else:
            return False

    def is_cyclic_util(self, v, visited, rec_stack):
        visited.add(v)
        rec_stack.add(v)

        for neighbor in self.adj_list [v]:
            if neighbor not in visited:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(v)
        return False

    def is_cyclic(self):
        visited = set()
        rec_stack = set()

        for v in self.adj_list:
            if v not in visited:
                if self.is_cyclic_util(v, visited, rec_stack):
                    return True

        return False



graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edges("A", "B")
graph.add_edges("A", "C")
graph.add_edges("A", "D")
graph.add_edges("B", "D")
graph.add_edges("C", "E")

# graph.print_graph()
# graph.remove_vertex("D")
graph.print_graph()

print("DFS:-")
graph.dfs("A")
print("\nBFS:-")
print( graph.bfs("A"))
graph.remove_vertex("C")
graph.dfs("A")
print()
print(graph.has_path_dfs("A","E"))
print()
print("check cycle :-")
print(graph.is_cyclic())
