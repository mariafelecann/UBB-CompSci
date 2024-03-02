from domain.graphs import Graph
from services.services import Service
import time

class UI:
    def __init__(self, n, m):
        service = Service(Graph(n, m))
        self.__graph = service
        self.__n = n
        self.__m = m

    def menu_for_users(self):
        print("options for working with graphs:")
        print(" 1 - add an vertex")
        print(" 2 - remove a vertex")
        print(" 3 - add an edge")
        print(" 4 - remove an edge")
        print(" 5 - get the number of vertices  ")
        print(" 6 - display the set of vertices")
        print(" 7 - verify if there is an edge between two vertices")
        print(" 8 - get the in degree of a specified vertex")
        print(" 9 - get the out degree of a specified vertex")
        print(" 10 - parse the set of outbound edges of a specified vertex")
        print(" 11 - parse the set of inbound edges of a specified vertex")
        print(" 12 - get the cost of an edge")
        print(" 13 - modify the cost of an edge")
        print(" 14 - read the graph from a text file ")
        print(" 15 - write the graph to a text file")
        print(" 16 - create a random graph with specified number of vertices and of edges")
        print(" 17 - breadth transversal search f connected components")
        print(" 18 - the lowest cost walk from a source vertex to a target vertex")
        print(" 19 - verify if the corresponding graph is a DAG and performs a topological sorting of the activities using the algorithm based on predecessor counters. \n      if it is a DAG, finds a highest cost path between two given vertices, in O(m+n).")
        print(" 0 - EXIT")

    def ui_add_vertex(self):
        vertex = input("please enter the vertex  --> ")
        try:
            vertex = int(vertex)
            if vertex < 0:
                print("vertex must be a positive number!")
                return
            if self.__graph.service_add_new_vertex(vertex) == 1:
                self.__n += 1
                print("done! :D vertex was added successfully ")
            else:
                print("oops! this vertex already exists! ")
        except ValueError:
            print("invalid data!")

    def ui_remove_vertex(self):
        vertex = input("what vertex do you want to remove? --> ")
        try:
            vertex = int(vertex)
            if vertex < 0:
                print("vertex must be a positive number!")
                return
            if self.__graph.service_remove_vertex(vertex):
                self.__n -= 1
                print("vertex was removed! :)")
            else:
                print("this vertex does not exist, so it cannot be removed :( ")
        except ValueError:
            print("invalid data!")

    def ui_add_edge(self):
        vertex_1 = input("enter the first vertex of your edge  -->  ")
        vertex_2 = input("enter the second vertex of your edge -->  ")
        try:
            vertex_1 = int(vertex_1)
            vertex_2 = int(vertex_2)
            if vertex_1 < 0 or vertex_2 < 0:
                print("vertex must be a positive number!")
                return
            cost = int(input("enter the cost of this edge -->  "))
            if self.__graph.service_add_edge(vertex_1, vertex_2, cost) == 1:
                print("done! edge was added!")
                self.__m += 1
            elif self.__graph.service_add_edge(vertex_1, vertex_2, cost) == -1:
                print("oops! this edge already exists!")
            elif self.__graph.service_add_edge(vertex_1, vertex_2, cost) == -2:
                print("oops! one or both of of the vertices you entered do not exist!")
        except ValueError:
            print("invalid data!")

    def ui_remove_edge(self):
        vertex_1 = input("enter the first vertex of your edge: ")
        vertex_2 = input("enter the second vertex of your edge: ")
        try:
            vertex_1 = int(vertex_1)
            vertex_2 = int(vertex_2)
            if vertex_1 < 0 or vertex_2 < 0:
                print("vertex must be a positive number!")
                return
            if self.__graph.service_remove_edge(vertex_1, vertex_2):
                print("edge was removed! :)")
                self.__m -= 1
            else:
                print("this edge does not exist, so it could not be removed! ")
        except ValueError:
            print("invalid data!")

    def ui_number_of_vertices(self):
        print("the number of vertices is: ", self.__graph.service_number_of_vertices())

    def ui_display_vertices(self):
        print("these are the vertices: ", self.__graph.service_get_vertices())

    def ui_verify_edge(self):
        print("please enter the vertices of your edge :D")
        vertex_1 = input("first vertex --> ")
        vertex_2 = input("second vertex --> ")
        try:
            vertex_1 = int(vertex_1)
            vertex_2 = int(vertex_2)
            if vertex_1 < 0:
                print("vertex must be a positive number!")
                return
            if vertex_2 < 0:
                print("vertex must be a posivie number!")
                return
            if self.__graph.service_verify_edge(vertex_1, vertex_2):
                print("yes, these two vertices construct an edge with the cost of ",
                      self.__graph.service_get_cost_of_edge(vertex_1, vertex_2))
            else:
                print("no, these two vertices do not construct an edge!")
        except ValueError:
           print("invalid data!")

    def ui_in_degree_of_vertex(self):
        vertex = input("please enter the vertex you want to see the in degree for --> ")
        try:
            vertex = int(vertex)
            if vertex < 0:
                print("vertex must be a positive number!")
                return
            in_degree, predecessor_vertices = self.__graph.service_in_degree(vertex)
            print("the in degree is : ", in_degree)
            print("the predecessor vertices that construct these edges are : ", predecessor_vertices)
        except ValueError:
            print("invalid data!")

    def ui_out_degree_of_vertex(self):
        vertex = input("please enter the vertex you want to see the out degree for --> ")
        try:
            vertex = int(vertex)
            if vertex < 0:
                print("vertex must be a positive number!")
                return
            out_degree, successor_vertices = self.__graph.service_out_degree(vertex)
            print("the out degree is : ", out_degree)
            print("the successor vertices that construct these edges are : ", successor_vertices)
        except ValueError:
            print("invalid data!")

    def ui_outbound_edges_of_vertex(self):
        vertex = input("please enter the vertex you want to see the outbound edges for --> ")
        try:
            vertex = int(vertex)
            if vertex < 0:
                print("vertex must be a positive number!")
                return
            successors = self.__graph.service_outbound_edges(vertex)
            if successors:
                print("the outbound edges of this vertex are: ")
                for successor_vertex in successors:
                    print("edge ", vertex, "->", successor_vertex)
            else:
                print("this vertex does not have any edges associated with it.")
        except ValueError:
            print("invalid data!")

    def ui_inbound_edges_of_vertex(self):
        vertex = input("please enter the vertex you want to see the inbound edges for --> ")
        try:
            vertex = int(vertex)
            if vertex < 0:
                print("vertex must be a positive number!")
                return
            predecessors = self.__graph.service_inbound_edges(vertex)
            if predecessors:
                print("the inbound edges of this vertex are: ")
                for predecessor_vertex in predecessors:
                    print("edge ", vertex, "<-", predecessor_vertex)
            else:
                print("this vertex does not have any edges associated with it.")
        except ValueError:
            print("invalid data!")

    def ui_get_cost_of_edge(self):
        print("please enter the vertices of your edge :D")
        vertex_1 = input("first vertex --> ")
        vertex_2 = input("second vertex --> ")
        try:
            vertex_1 = int(vertex_1)
            vertex_2 = int(vertex_2)
            if vertex_1 < 0 or vertex_2 < 0:
                print("vertex must be a positive number!")
                return
            if self.__graph.service_get_cost_of_edge(vertex_1, vertex_2) != -1:
                print("the cost of this edge is", self.__graph.service_get_cost_of_edge(vertex_1, vertex_2))
            else:
                print("this edge does not have a cost!")
        except ValueError:
            print("invalid data!")

    def ui_change_cost_of_edge(self):
        print("please enter the vertices of your edge :D")
        vertex_1 = input("first vertex --> ")
        vertex_2 = input("second vertex --> ")
        new_cost = input("enter the new cost of this edge --> ")
        try:
            vertex_1 = int(vertex_1)
            vertex_2 = int(vertex_2)
            if vertex_1 < 0 or vertex_2 < 0:
                print("vertex must be a positive number!")
                return
            new_cost = int(new_cost)
            if self.__graph.service_change_cost_of_edge(vertex_1, vertex_2, new_cost) != -1:
                print("done! the new cost was updated!")
            else:
                print("this edge does not have a cost!")
        except ValueError:
            print("invalid data!")

    def ui_read_from_file(self):
        file = input("enter the name of the file you want to read from: --> ")
        graph, n, m, success = self.__graph.read_from_file(file)
        if success:
            print("the graph that was read from the file has the following vertices: ")
            new_service = Service(graph)
            new_service.set_number_edges(m)
            new_service.set_number_of_vertices(n)
            print(new_service.service_get_vertices())
            print("do you want to perform operations on this graph? yes/no")
            while True:
                choice = input("-->")
                if choice == "yes":
                    self.__graph = new_service
                    self.__n = n
                    self.__m = m
                    break
                elif choice == "no":
                    break
                else:
                    print("invalid choice! try again")
        else:
            print("there was an error in reading from file.")

    def ui_write_to_file(self):
        file = input("enter the name of the file: ")
        with open(file, "w") as f:
            f.write(str(self.__n))
            f.writelines(" ")
            f.writelines(str(self.__m))

        with open(file, "a") as f:
            for i in self.__graph.get_cost():
                f.writelines("\n")
                vertex1, vertex2 = int(i[0]), int(i[1])
                f.writelines(str(vertex1))
                f.writelines(" ")
                f.writelines(str(vertex2))
                f.writelines(" ")
                f.writelines(str(self.__graph.service_get_cost_of_edge(vertex1, vertex2)))

        print("file updated! :D")

    def ui_create_random_graph(self):
        n = input("how many vertices? --> ")
        m = input("how many edges? --> ")
        try:
            n = int(n)
            m = int(m)
            if n < 0:
                print("number of vertices must be a positive number! ")
                return
            if m < 0 or m > n*(n-1):
                print("number of edges must be a positive number that is maximum n*(n-1), "
                      "where n is the number of vertices!")
                return
            graph = self.__graph.services_create_random_graph(n, m)
            print("your random graph has ", n, " vertices and ", m, " edges! ")
            print("the edges are: ", graph.get_edges())
            print("do you want to do operations on this graph? yes/no")
            while True:
                choice = input("-->")
                if choice == "yes":
                    service_graph = Service(graph)
                    self.__graph = service_graph
                    self.__n = n
                    self.__m = m
                    break
                elif choice == "no":
                    break
                else:
                    print("invalid choice! try again")
        except ValueError as ve:
            print("invalid input")

    def ui_breadth_transversal(self):
        print(self.__graph.bfs_connected_components())

    def ui_transform_into_undirected_graph(self):
        undirected_graph = self.__graph
        edges = undirected_graph.service_get_edges()
        index = 0
        for pair in edges:
            vertex1, vertex2 = pair
            undirected_graph.service_add_edge(vertex2, vertex1, 0)
            index += 1
        print("transforming the graph to be undirected")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("the graph you use has been transformed into an undirected graph! :)")
        self.__graph = undirected_graph
        self.__m = self.__m * 2

    def dijkstra_ui(self):
        source = int(input("what is the source vertex?"))
        target = int(input("what is the target vertex?"))
        cost, components = self.__graph.dijkstra_good(source, target)
        print("the lowest cost walk is: ", cost, "and the components are: ", components)

    def topologically_sorted_ui(self):
        is_dag = self.__graph.verify_dag()
        print("is DAG:", is_dag)

        if is_dag:
            sorted_order = self.__graph.topological_sort()
            print("topological sort:", sorted_order)

            print("now let's compute the highest cost walk between two vertices! :D")
            start_vertex = int(input("enter the starting vertex --> "))
            end_vertex = int(input("enter the end vertex --> "))
            highest_cost = self.__graph.highest_cost_path(start_vertex, end_vertex)
            print(f"highest cost path from {start_vertex} to {end_vertex} is:", highest_cost)

    def start_ui(self):
        choices = {
            "1": self.ui_add_vertex,
            "2": self.ui_remove_vertex,
            "3": self.ui_add_edge,
            "4": self.ui_remove_edge,
            "5": self.ui_number_of_vertices,
            "6": self.ui_display_vertices,
            "7": self.ui_verify_edge,
            "8": self.ui_in_degree_of_vertex,
            "9": self.ui_out_degree_of_vertex,
            "10": self.ui_outbound_edges_of_vertex,
            "11": self.ui_inbound_edges_of_vertex,
            "12": self.ui_get_cost_of_edge,
            "13": self.ui_change_cost_of_edge,
            "14": self.ui_read_from_file,
            "15": self.ui_write_to_file,
            "16": self.ui_create_random_graph,
            "17": self.ui_breadth_transversal,
            "18": self.dijkstra_ui,
            "19": self.topologically_sorted_ui}
        while True:
            print("WELCOME")
            self.menu_for_users()
            choice = input("please enter your choice : ")
            if choice in choices:
                choices[choice]()
            elif choice == "0":
                break
            elif int(choice) > 18:
                print("oops! invalid choice :/ please try again!")
