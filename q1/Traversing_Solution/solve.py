class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, s, d):
        if(s not in self.graph):
            self.graph[s] = []
        if(d not in self.graph):
            self.graph[d] = []
        self.graph[s].append(d)
        self.graph[d].append(s)

    def print_graph(self):
        for i in self.graph:
            print("%s: -> %s" % (i, self.graph[i]))

    def traversing_cycles(self):
        return self.traversing_cyclesR('A')

    def traversing_cyclesR(self, node):
        
        cont = 0
        visited = set()
        remaining = [node]

        while remaining:
            current = remaining.pop()
            visited.add(current)

            for vizinho in self.graph[node]:
                if vizinho in visited:
                    cont += 1
                
                remaining.append(vizinho)
                
        return cont

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')

    print(graph.traversing_cycles())