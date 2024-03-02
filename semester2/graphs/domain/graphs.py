from random import randint
from exceptions.exceptions import *


class Graph:
    def __init__(self, n, m):
        self.__number_of_vertices = n
        self.__number_of_edges = m
        self.__vertices = []
        self.__list_of_predecessors = []
        self.__list_of_successors = []
        self.__cost = dict()

        for i in range(n):
            self.add_vertex(i)
            self.__list_of_successors.append([])
            self.__list_of_predecessors.append([])

    # existence methods

    def is_vertex(self, vertex):
        return vertex in self.__vertices

    def is_edge(self, vertex_1, vertex_2):
        for vertex in self.__list_of_predecessors[vertex_2]:
            if vertex == vertex_1:
                return True

        for vertex in self.__list_of_successors[vertex_1]:
            if vertex == vertex_2:
                return True

    # add methods

    def add_vertex(self, vertex):
        if self.is_vertex(vertex):
            return -1
        self.__number_of_vertices += 1
        self.__vertices.append(vertex)
        self.__list_of_predecessors.insert(vertex, [])
        self.__list_of_successors.insert(vertex, [])
        return 1

    def add_edge(self, vertex_1, vertex_2, edge_cost):
        if self.is_edge(vertex_1, vertex_2):
            return -1
        if not self.is_vertex(vertex_1):
            return -2
        if not self.is_vertex(vertex_2):
            return -2
        self.__number_of_edges += 1
        self.__list_of_predecessors[vertex_2].append(vertex_1)
        self.__list_of_successors[vertex_1].append(vertex_2)
        self.__cost[(vertex_1, vertex_2)] = edge_cost
        return 1

    # remove methods

    def remove_edge(self, vertex_1, vertex_2):
        if not self.is_edge(vertex_1, vertex_2):
            return -1
        del self.__cost[(vertex_1, vertex_2)]
        for vertex in self.__list_of_successors[vertex_1]:
            if vertex == vertex_2:
                del vertex
        for vertex in self.__list_of_predecessors[vertex_2]:
            if vertex == vertex_1:
                del vertex
        self.__number_of_edges -= 1
        return 1

    def remove_vertex(self, vertex_to_remove):
        if not self.is_vertex(vertex_to_remove):
            return -1
        for listt in self.__list_of_successors:
            for vertex in listt:
                if vertex == vertex_to_remove:
                    del vertex
        del self.__list_of_successors[vertex_to_remove]
        for listt in self.__list_of_predecessors:
            for vertex in listt:
                if vertex == vertex_to_remove:
                    del vertex
        self.__list_of_predecessors[vertex_to_remove] = []
        self.__list_of_successors[vertex_to_remove] = []
        del self.__vertices[vertex_to_remove]
        return 1

    # getters and setters

    def get_edge_cost(self, vertex1, vertex2):
        if (vertex1, vertex2) not in self.__cost:
            return -1
        return self.__cost[(vertex1, vertex2)]

    def set_edge_cost(self, vertex1, vertex2, new_cost):

        if (vertex1, vertex2) not in self.__cost:
            return -1
        self.__cost[(vertex1, vertex2)] = new_cost

    def get_number_of_vertices(self):
        return self.__number_of_vertices

    def get_vertices(self):
        return self.__vertices

    def get_predecessors(self):
        return self.__list_of_predecessors

    def get_successors(self):
        return self.__list_of_successors

    def get_number_of_edges(self):
        return self.__number_of_edges

    def get_cost_list(self):
        return self.__cost

    def set_number_vertices(self, n):
        self.__number_of_vertices = n

    def set_number_edges(self, m):
        self.__number_of_edges = m

    def get_edges(self):
        list_of_edges = []
        list_of_costs = []
        for edge, cost in self.__cost.items():
            vertex1, vertex2 = edge
            list_of_edges.append([vertex1, vertex2])
            list_of_costs.append(cost)
        return list_of_edges
