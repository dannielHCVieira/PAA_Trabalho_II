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
        colors = {}
        parents = {}
        for v in self.graph:
            colors[v] = 0 
        return self.traversing_cyclesR('A', '', colors, parents)

    def traversing_cyclesR(self, node, parent, colors, parents):
        
        cont = 0

        if(colors[node] == 2):
            return 0
        
        if(colors[node] == 1):
            cont = 1
        
        if(parent != ''):
            parents[node] = parent
        
        colors[node] = 1

        for v in graph[node]:
            if(v == parents[node]):
                continue
            cont += self.traversing_cyclesR(v, node, colors, parents)

        colors[node] = 2
        
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