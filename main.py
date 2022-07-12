import copy
import time
import random

class Graph:

    def __init__(self, n):
        self.vertices = dict()
        for i in range(n):
            self.vertices[i] = (set())
        self.edges=dict()

    def add_edge(self, x, y,c):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if c==0:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y)  in self.edges or str(x)+"-"+str(y) in self.edges:
            print("Edge already there!")
            return
        if x==y:
            return
        self.vertices[x].add(y)
        self.vertices[y].add(x)
        self.edges[str(x)+"-"+str(y)]=c
    def remove_edge(self,x,y):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges and str(y)+"-"+str(x) not in self.edges:
            print("Invalid input!")
            return
        self.vertices[x].remove(y)
        self.vertices[y].remove(x)
        ok=str(x)+"-"+str(y) not in self.edges
        if ok==0:
            self.edges.pop(str(x) + "-" + str(y))
        else:
            self.edges.pop(str(y) + "-" + str(x))
    def add_vertex(self):
        self.vertices[self.get_nr_of_vertices()+1]=set()
    def delete_vertex(self,x):
        if x not in self.vertices:
            print("Invalid input!")
            return
        new_dic=dict()
        l=self.parse_vertices()
        for i in l:
            if x in self.vertices[i]:
                self.vertices[i].remove(x)
        del self.vertices[x]
        for key in self.edges:
            if int(key[0])==int(x) or int(key[2])==int(x):
                pass
            else:
                new_dic[key]=self.edges[key]

        self.edges=copy.deepcopy(new_dic)
    def is_edge(self, x, y):

        if (y in self.vertices[x]):
            return 1
        else:
            return 0

    def get_cost(self,x,y):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges and str(y)+"-"+str(x) not in self.edges:
            print("Invalid input!")
            return
        ok=str(x)+"-"+str(y) not in self.edges
        if ok==0:
            return self.edges[str(x)+"-"+str(y)]
        else:
            return self.edges[str(y) + "-" + str(x)]
    def set_cost(self,x,y, new):
        if x not in self.vertices:
            print("Invalid input!")
            return
        if y not in self.vertices:
            print("Invalid input!")
            return
        if new ==0:
            print("Invalid input!")
            return
        if str(x)+"-"+str(y) not in self.edges and str(y)+"-"+str(x) not in self.edges:
            print("Invalid input!")
            return
        ok = str(x) + "-" + str(y) not in self.edges
        if ok == 0:
            self.edges[str(x)+"-"+str(y)] = new
        else:
            self.edges[str(y) + "-" + str(x)] = new
    def parse_vertices(self):
        vertices_list = list()
        for key in self.vertices:
            vertices_list.append(key)
        return vertices_list

    def parse_neighbours(self, x):
        if x not in self.vertices:
            print("Invalid input!")
            return
        nout_vertices = list()
        for y in self.vertices[x]:
            nout_vertices.append(y)
        return nout_vertices

    def get_nr_of_vertices(self):
        return len(self.vertices)
    def get_nr_of_edges(self):
        return len(self.edges)
    def get_degree(self,x):
        if x not in self.vertices:
            print("Invalid input!")
            return

        return len(self.vertices[x])

    def copy(self):
        n=copy.deepcopy(self)
        return n
    def get_edges(self):
        return self.edges

def print_graph(g):
    print("Neighbors:")
    for x in g.parse_vertices():
        s = str(x) + ":"

        for y in g.parse_neighbours(x):
            s = s + " " + str(y)
        print(s)

def dfs(g,start,visited,comp):


    for y in g.parse_neighbours(start):
        if y not in visited:
            visited.append(y)
            comp.append(y)
            dfs(g,y,visited,comp)
    return comp
def f(g,visited,comp):
    d=dict()
    k=1
    for v in g.parse_vertices():
        if v not in visited:
            visited.append(v)
            comp.append(v)
            d[k]=dfs(g,v,visited,comp)
            comp=[]
            k+=1
    return d
def create_random_graph(n, m):
    g = Graph(n)
    while m > 0:
        x = random.randrange(n)
        y = random.randrange(n)
        if x!=y and g.is_edge(x, y)==0:
            g.add_edge(x, y,random.randint(2,20))
            m = m - 1
    return g
def print_menu():
    print("0. Exit")
    print("1. Add edge")
    print("2. Remove edge")
    print("3. Add vertex")
    print("4. Remove vertex")
    print("5. Get cost of edge")
    print("6. Set cost of edge")
    print("7. Get nr of vertices")
    print("8. Get nr of edges")
    print("9. Parse all vertices")
    print("10. Parse neighbours")
    print("11. Print graph")
    print("12. Get degree")
    print("14. See components")

def start(g):
    while True:
        print("\n")
        print_menu()
        opt = input()
        if opt == "1":
            x = input("Give the x: ")
            y = input("Give the y: ")
            c=input("Give the cost: ")
            g.add_edge(int(x),int(y),int(c))

        elif opt == "2":
            x = input("Give the x: ")
            y = input("Give the y: ")
            g.remove_edge(int(x),int(y))

        elif opt == "3":
            g.add_vertex()
        elif opt == "4":
            x = input("Give the x: ")
            g.delete_vertex(int(x))

        elif opt == "5":
            x = input("Give the x: ")
            y = input("Give the y: ")
            print(g.get_cost(int(x),int(y)))
        elif opt == "6":
            x = input("Give the x: ")
            y = input("Give the y: ")
            n=input("New cost is: ")
            g.set_cost(int(x),int(y),int(n))
        elif opt == "7":
            print(g.get_nr_of_vertices())
        elif opt == "8":
            print(g.get_nr_of_edges())
        elif opt == "9":
            l=g.parse_vertices()
            for i in l:
                print(i)
        elif opt == "10":
            x= input("Give x: ")
            l=g.parse_neighbours(int(x))
            for i in l:
                print(i)
        elif opt == "11":
            print_graph(g)
        elif opt == "12":
            x = input("Give x: ")
            print(g.get_degree(int(x)))
        elif opt=="14":
            spec(g)
        elif opt=="0":
            return
def spec(g):
    visited = []
    c = []
    d = f(g, visited, c)
    for key in d:
        print(key)
        print(d[key])

def isCyclicUtil(g, v, visited, parent):
        visited[v] = True
        for i in g.parse_neighbours(v):
            if visited[i] == False:
                if (isCyclicUtil(g,i, visited, v)):
                    return True
            elif parent != i:
                return True
        return False
    # Returns true if the graph contains a cycle, else false.
def isCyclic(g):
        visited = [False] * (g.get_nr_of_vertices())
        for i in range(g.get_nr_of_vertices()):
            if visited[i] == False:
                if (isCyclicUtil(g,i, visited, -1)) == True:
                    return True
        return False
def kruskal(g):

    tree=Graph(g.get_nr_of_vertices())
    costs=[]
    edges=[]

    for edge in g.get_edges():
        costs.append(int(g.get_edges()[edge]))
        edges.append(edge)
    for i in range(0,len(costs)):
        for j in range(0, len(costs)):
            if costs[i]<costs[j]:
                costs[i],costs[j]=costs[j],costs[i]
                edges[i],edges[j]=edges[j],edges[i]


    for i in range(0, len(costs)):
            tree.add_edge(int(edges[i][0]),int(edges[i][2]),costs[i])
            if isCyclic(tree)==True:
                tree.remove_edge(int(edges[i][0]),int(edges[i][2]))
    return tree
def main():
    g = Graph(5)
    tree=Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(0, 3, 1)
    g.add_edge(1, 2, -3)
    g.add_edge(1,3,5)
    g.add_edge(2,3,2)

   # print(isCyclic(g))

    #kruskal(g)
    tree=kruskal(g)
    start(tree)
    #g=read_textfile("random_graph1.txt")
    #start(g)
    #print_graph(g)
    # parse_graph(g)


main()