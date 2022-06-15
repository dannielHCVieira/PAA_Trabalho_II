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
            else:
                perm.append(v)
                cont += self.permutation_cyclesR(self.graph[v], perm)
                perm.pop()
        return cont

    def DFS_cyclesR(self, v, visited, parent):
        c = 0

        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                c += self.DFS_cyclesR(i, visited, v)

            elif parent != i:
                c += 1
 
        return c
 
    def DFS_cycles(self):
        c = 0
        self.numComparison = 0
        start_time = time.time_ns()
        visited = {}
        for k in self.graph.keys():
            visited[k] = False
 
        for k in self.graph.keys():
            if visited[k] == False:
                c += self.DFS_cyclesR(k, visited, -1)

        end_time = time.time_ns()
        print("Time of Execution: {}".format((end_time - start_time) / 10**6))
        return c

if __name__ == "__main__":
    print("Counting cycles in undirected graph.\n")
    op = int(input("1 - Automatic edges insertion\n2 - Manual edges insertion\n0 - Exit\n>>> "))
    while op != 0:
        graph = Graph()
        if op == 1:
            n = int(input("How many vertex? "))
            for i in range(0, n):
                for j in range(i+1, n):
                    graph.add_edge("e{}".format(i),"e{}".format(j))
            print("Number of cycles: {}".format(graph.permutation_cycles()))
            print("Number of comparisons: {}".format(graph.numComparison))
        elif op == 2:
            while True:
                e1, e2 = input("Input edge (edge A, edge B) (, to escape): ").split(",")
                if len(e1) == 0:
                    break
                e1 = e1.strip()
                e2 = e2.strip()
                graph.add_edge(e1, e2)

            print("Number of cycles: {}".format(graph.permutation_cycles()))
            print("Number of comparisons: {}".format(graph.numComparison))
        else:
            print("Invalid operation")
        op = int(input("1 - Automatic edges insertion\n2 - Manual edges insertion\n0 - Exit\n>>> "))

        