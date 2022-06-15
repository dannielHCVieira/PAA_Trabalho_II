import time
class Graph:
    def __init__(self):
        self.graph = {}
        self.numComparison = 0

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
        self.numComparison = 0
        start_time = time.time_ns()
        qtd = self.permutation_cyclesR(self.graph, [])
        end_time = time.time_ns()
        print("Time of Execution: {}".format((end_time - start_time) / 10**6))
        return qtd

    def permutation_cyclesR(self, li, perm):
        cont = 0
        
        for v in li:
            if(v in perm):
                if(v == perm[0] and len(perm) > 2):
                    cont += 1
                self.numComparison += 3
            else:
                perm.append(v)
                cont += self.permutation_cyclesR(self.graph[v], perm)
                perm.pop()
            self.numComparison += 1
        return cont

if __name__ == "__main__":
    graph = Graph()
    print("Counting cycles in undirected graph.\n")
    while True:
        e1, e2 = input("Input edge (edge A, edge B) (, to escape): ").split(",")
        if len(e1) == 0:
            break
        e1 = e1.strip()
        e2 = e2.strip()
        graph.add_edge(e1, e2)

    print("Number of cycles: {}".format(graph.permutation_cycles()))
    print("Number of comparisons: {}".format(graph.numComparison))