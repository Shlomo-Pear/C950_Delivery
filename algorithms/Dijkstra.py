"""
Dijkstra's Shortest Path Algorithm

Abandoned
"""


# Ref: WGU Webinar: How to Dijkstra?; https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=aad71bd6-abf5-4cd4-8a78-ac7f01039c73
class Vertex:

    # Constructor for a new vertex object. All vertex objects start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

# ----------------------------------------------------------

class Graph:
    def __init__(self):
        self.adjacency_list = {}  # vertex dictionary {key:value}
        self.edge_weights = {}  # edge dictionary {key:value}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight

        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

# ----------------------------------------------------------
def dijkstra_shortest_path(g, start_vertex):
    # Put all vertices in an unvisited queue.
    unvisited_queue = []

    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # Start vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is empty.
    while len(unvisited_queue > 0):

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            # print(unvisited_queue[i].label, unvisited_queue[i].distance, unvisited_queue[i].pred_vertex)
            if unvisited_queue[1].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        # print("From Start Vertex to current_vertex.label: " + current_vertex.label + " distance: " + str(current_vertex.distance))

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:  # values from dictionary

            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]  # values from dictionary
            alternative_path_distance = current_vertex.distance + edge_weight

            # If a shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex

# ----------------------------------------------------------

def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = "-> " + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path
# ----------------------------------------------------------

def get_shortest_path_city(hash_table, start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        myPkgObj = hash_table.search(int(current_vertex.label))
        path = " -> " + myPkgObj.city + path
        current_vertex = current_vertex.pred_vertex
    path = "Salt Lake City " + path
    return path
# ----------------------------------------------------------

def dijkstraAlgShortestPath(hashTable):  #todo
    # Dijkstra's Shortest Path main
    # Program to find the shortest paths from vertex A.
    g = Graph()

    #add Vertices
    vertex_1 = Vertex("1")
    g.add_vertex(vertex_1)
    vertex_2 = Vertex("2")
    g.add_vertex(vertex_2)
    vertex_3 = Vertex("3")
    g.add_vertex(vertex_3)
    vertex_4 = Vertex("4")
    g.add_vertex(vertex_4)
    # etc.

    # add Edges
    g.add_undirected_edge(vertex_1, vertex_2, 484)
    g.add_undirected_edge(vertex_3, vertex_4, 626)
    # etc.

    # Run Dijkstra's algorithm first.
    dijkstra_shortest_path(g, vertex_1)

    # Get the vertices by the label for convenience; display the shortest path for each vertex
    # From vertex_1
    print("\nDijkstra's Shortest Path:")
    for v in g.adjacency_list:
        if v.pred_vertex is None and v is not vertex_1:
            print(f"1 to {v.label} ==> no path exists")
        else:
            print(f"1 to {v.label} ==> {get_shortest_path(vertex_1, v)} (total distance: {v.distance})")

    print("\nDijkstra's Shortest Path with Cities:")
    for v in g.adjacency_list:
        myPkgObj = hashTable.search(int(v.label))
        if v.pred_vertex is None and v is not vertex_1:
            print(f"Salt Lake City to {myPkgObj.city} ==> no path exists")
        else:
            print(f"Salt Lake City to {myPkgObj.city} ==> {get_shortest_path_city(vertex_1, v)} (total distance: {v.distance})")

