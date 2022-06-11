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

    def permutation_cycles(self):
        return self.permutation_cyclesR(self.graph, [])

    def permutation_cyclesR(self, li, perm):
        cont = 0
        
        for v in li:
            if(v in perm):
                if(v == perm[0] and len(perm) > 2):
                    cont += 1
                    
            else:
                perm.append(v)
                cont += self.permutation_cyclesR(self.graph[v], perm)
                perm.pop()
                
        return cont

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')

    print(graph.permutation_cycles())