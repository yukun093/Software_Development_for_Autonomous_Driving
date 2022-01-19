"""
Goal of Task 1:
    Get an overview of how a simple graph class can be implemented. This is a precondition to perform the dijkstra's
    or A* Algorithm. We need to extract the raw data of the map and use it to perform the optimization.

Hint:
    This is a very simple example of how the edges can be represented. In industrial applications more complicated
    raw data is used.
"""


class Graph:
    def __init__(self, map_raw_data):
        """
        This function reads out our map information. The map is defined via edges and their costs.
        The first location in the .txt-file is the start location of an edge and the second the goal location.
        The number after these two locations on the edge is the cost value to get from start to goal.
        """

        graph_edges = []

        # Subtask 1:
        # ToDo: extract the information of the .txt-file
        # Hints:
        #   - The result should be a list of tuples:  graph_edges =[('LocationA_from', 'Location_to', distance), ...]
        #   - The output are the edges from A to B and the corresponding distance for this edge.
        ########################
        #  Start of your code  #
        ########################
        for line in open(map_raw_data):
            line = line.strip('\n')
            data = line.split(' ')
            data = tuple(data)
            graph_edges.append(data)  # [('LocationA_from', 'Location_to', distance), ...]

        ########################
        #   End of your code   #
        ########################

        self.nodes = set()
        self.neighbors_list = set()
        # Subtask 2:
        # ToDo: add two more attributes (self.nodes and self.neighbors_list) to the class
        # Hints:
        #   - self.nodes --> set of strings {'Location1', 'Location2', ...}
        #   - self.neighbors_list saves all adjacent nodes for every node and the distance to them. It should be
        #   realised as a dict of sets. The sets contain tuples of the form --> (str('Location'), float(distance)).
        #   Example:
        #   self.neighbors_list --> dict: {'Location1': {('Location_x', distance_to_x),('Location_y', distance_to_y)...
        #                                  'Location2': {('Location_z', distance_to_z),('Location_p', distance_to_p)...
        #                                   ...}
        ########################
        #  Start of your code  #
        ########################
        for line in open(map_raw_data):
            line = line.strip('\n')
            data = line.split(' ')
            for element in data:
                if element.isdigit():
                    pass
                else:
                    self.nodes.add(element)

        for node in self.nodes:  # every city in the loop
            sub_neighbors_set = set()
            location_x = ''
            distance_to_x = 0  # init a distance between two cities
            flag = 0
            for line in open(map_raw_data):
                line = line.strip('\n')
                line = line.split(' ')  # every line in the munich file
                for element in line:  # check if the node in the every line
                    if node == element:
                        flag = 1
                if flag == 1:  # if it is in one line, extract the useful information
                    for element in line:
                        if element.isdigit():
                            distance_to_x = float(element)
                        else:
                            if node != element:
                                location_x = element
                    sub_sub_neighbors_list = (location_x, distance_to_x)  # ('Location_x', distance_to_x), type: tuple
                    sub_neighbors_set.add(sub_sub_neighbors_list)
                flag = 0
            self.neighbors_list = dict(self.neighbors_list)
            self.neighbors_list[node] = sub_neighbors_set
        ########################
        #   End of your code   #
        ########################


def generate_graph(file):
    graphs = Graph(file)
    return graphs


if __name__ == "__main__":
    graph = generate_graph("munich.txt")
    print(graph.nodes)
    print(graph.neighbors_list)
    """ The print functions should print the existing locations/nodes (graph.nodes)
     and the nodes (graph.neighbors_list) with all neighbors and the distance to them """
