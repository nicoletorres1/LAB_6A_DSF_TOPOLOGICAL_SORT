'''
Author: Nicole Torres
CS2302: LAB 6A
Purpose: To implement dsf and topological sort
last modification: 12/04/18
'''
import time


debug = False


class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        return self.find(self.dsf[a])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        self.dsf[rb] = ra

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def get_num_trees(self):
        count = 0

        for num in self.dsf:
            if False:  # TODO: Replace False with your answer
                count += 1

        return count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_leaf(self, k):
        for num in self.dsf:
            if False:  # TODO: Replace False with your answer
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def is_compressed(self):

        # TODO: Loop missing

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def create_dsf(n, k):
        dsf = [1234] * n # TODO: Replace 1234 with your answer

        # TODO: One line missing (No need to add more than 1 line)

        return dsf

    def print(self):
        print(self.dsf)

def kruskalMST(graph):
    """
    This method, given an undirected graph with
    no self loops, returns the MST made from
    that graph.
    :param graph:
    :return:
    """

    # MST must have just as many vertices
    vertices = len(graph)
    mst = []
    for vertex in range(vertices):
        mst.append([0]*vertices)

    dsf = DisjointSetForest(len(graph))

    edges = []
    for u in range(0,len(graph)):
        for v in range(u+1,len(graph)):
            weight = graph[u][v]
            if weight != 0:
                # There's an edge here!
                edge = {"vertices":(u,v), "weight":weight}  # using list to store vertices since order does matter later
                edges.append(edge)

    edges = sorted(edges, key=lambda x: x["weight"])

    for edge_index in range(len(edges)):
        edge = edges[edge_index]
        u = edge["vertices"][0]
        v = edge["vertices"][1]
        w = edge["weight"]
        if dsf.find(u) != dsf.find(v):
            # Throw edge in the graph
            mst[u][v] = w
            mst[v][u] = w
            if debug: print("%d != %d, weight = %d, mst_uv = %d, mst_vu = %d"%(u,v,edge["weight"], mst[u][v], mst[v][u]))
            dsf.union(u,v)

    return mst


# Class I need before starting topological sort
class DFSVertex:
    def __init__(self):
        self.predecessor = -1
        self.color = 'white'
        self.discovery_time = -1
        self.finish_time = -1

time = 0
vertices = {}  # empty dictionary {vertex_num : vertex object}
sorted_vertices = []


def DFS_visit(adjMat, vertex_num):
    global time, vertices, sorted_vertices
    time += 1
    vertices[vertex_num].discovery_time = time
    vertices[vertex_num].color = 'gray'
    for neighbor in range(len(adjMat)):
        if adjMat[vertex_num][neighbor] != 0:
            # then there's an edge between vertex_num and neighbor
            if vertices[neighbor].color == 'white':
                vertices[neighbor].predecessor = vertex_num
                DFS_visit(adjMat, neighbor)
    vertices[vertex_num].color = 'black'
    time += 1
    vertices[vertex_num].finish_time = time
    sorted_vertices.insert(0, vertex_num)


def topologicalSort_AdjMat(adjMat):
    global time, vertices, sorted_vertices

    # TOPOLOGICAL SORT ALGORITHM
    # Call DFS, compute finishing times
    # As each vertex is finished, insert into front of linked list
    # return linked list of vertices

    vertices = {} # initialize global dictionary
    sorted_vertices = [] # initialize global sorted list

    # DFS
    for vertex_num in range(len(adjMat)):
        vertices[vertex_num] = DFSVertex()  # Initialization of the vertices
    time = 0
    for vertex_num in range(len(adjMat)):
        if vertices[vertex_num].color == 'white':
            DFS_visit(adjMat, vertex_num)

    return sorted_vertices


if __name__ == '__main__':

    # Hard Coded Graphs
    graph = [
        [0,2,8,0,0],
        [2,0,0,4,0],
        [8,0,0,1,5],
        [0,4,1,0,3],
        [0,0,5,3,0]
    ]

    top_sort_graph = [
        [0,1,1,0],
        [0,0,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ]

    top_sort_graph2 = [
        [0,0,0,1,0],
        [0,0,0,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0]
    ]

    sorted_list = topologicalSort_AdjMat(top_sort_graph2)
    print('RESULT :', sorted_list)

    # print('\n' "<<< %s seconds >>>" '\n' % (time.time() - start_time))

    # future note-- Practice to encode the above graph as an adjaceny list and an edge list

    # mst = kruskalMST(graph)
    #
    # for row in mst:
    #     print(row)








