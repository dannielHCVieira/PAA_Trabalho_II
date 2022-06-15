from stringprep import c22_specials


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
        print("node ",node)
        print("Graph ",self.graph[node])
        print("Parents ",parents)

        for v in self.graph[node]:
            if(v == parents[node]):
                continue
            cont += self.traversing_cyclesR(v, node, colors, parents)

        colors[node] = 2
        
        return cont

    def DFSCycle(self):
        colors = {}
        parents = {}
        for v in self.graph:
            colors[v] = 0
        return self.DFSCycleR(list(self.graph)[0], '', colors, parents) 
    
    def DFSCycleR(self, u, p, color, par):
        c = 0
        if color[u] != 2:
            if color[u] != 1:
                par[u] = p
                color[u] = 1

                for v in self.graph[u]:
                    if v == par[u]:
                        c += self.DFSCycleR(v, u, color, par) 
            else:
                return 1
        return c
        
    def DFS_CyclesR(self, v, visited, parent):
        c = 0

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                c += self.DFS_CyclesR(i, visited, v)

            elif parent != i:
                c += 1
 
        return c
 
    def DFS_Cycles(self):
        c = 0

        visited = {}
        for k in self.graph.keys():
            visited[k] = False
 
        for k in self.graph.keys():
            if visited[k] == False:
                c += self.DFS_CyclesR(k, visited, -1)
                """ if(self.DFS_CyclesR
                   (i, visited, -1)) == True:
                    return True """
        return c

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')

    print(graph.DFS_Cycles())