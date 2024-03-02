from domain.graphs import Graph
from random import randint
from collections import deque
from heapq import heappush, heappop
from math import inf


class Service:

    def __init__(self, graph):
        self.__service_graph = graph

    def service_add_new_vertex(self, vertex):
        if self.__service_graph.add_vertex(vertex) == 1:
            return 1
        return 0

    def service_remove_vertex(self, vertex):
        if self.__service_graph.remove_vertex(vertex) == 1:
            return 1
        return 0

    def service_add_edge(self, vertex_1, vertex_2, cost):
        if self.__service_graph.add_edge(vertex_1, vertex_2, cost) == 1:
            return 1
        if self.__service_graph.add_edge(vertex_1, vertex_2, cost) == -1:
            return -1
        if self.__service_graph.add_edge(vertex_1, vertex_2, cost) == -2:
            return -2

    def service_remove_edge(self, vertex_1, vertex_2):
        if self.__service_graph.remove_edge(vertex_1, vertex_2) == 1:
            return 1
        return 0

    def service_number_of_vertices(self):
        return self.__service_graph.get_number_of_vertices()

    def service_get_vertices(self):
        return self.__service_graph.get_vertices()

    def service_verify_edge(self, vertex_1, vertex_2):
        if self.__service_graph.is_edge(vertex_1, vertex_2):
            return True
        else:
            return False

    def service_get_cost_of_edge(self, vertex_1, vertex_2):
        return self.__service_graph.get_edge_cost(vertex_1, vertex_2)

    def service_in_degree(self, vertex):
        return len(self.__service_graph.get_predecessors()[vertex]), self.__service_graph.get_predecessors()[vertex]

    def service_out_degree(self, vertex):
        return len(self.__service_graph.get_successors()[vertex]), self.__service_graph.get_successors()[vertex]

    def service_outbound_edges(self, vertex):
        return self.__service_graph.get_successors()[vertex]

    def service_inbound_edges(self, vertex):
        return self.__service_graph.get_predecessors()[vertex]

    def service_change_cost_of_edge(self, vertex_1, vertex_2, new_cost):
        self.__service_graph.set_edge_cost(vertex_1, vertex_2, new_cost)

    def set_number_of_vertices(self, n):
        self.__service_graph.set_number_vertices(n)

    def set_number_edges(self, m):
        self.__service_graph.set_number_edges(m)

    def get_cost(self):
        return self.__service_graph.get_cost_list()

    def read_from_file(self, file_name):
        file = open(file_name, "r")
        n, m = map(int, file.readline().split())
        g = Graph(n, m)
        success = 0
        for _ in range(m):
            vertex1, vertex2, edge_cost = map(int, file.readline().split())
            success = g.add_edge(vertex1, vertex2, edge_cost)
        file.close()
        return g, n, m, success

    def services_create_random_graph(self, n, m):
        random_graph = Graph(n, m)
        number_of_edges_added = 0
        while number_of_edges_added < m:
            if random_graph.add_edge(randint(0, n - 1), randint(0, n - 1), randint(0, 2000)) == 1:
                number_of_edges_added += 1
        return random_graph

    def enqueue(self, queue, x):
        queue.append(x)

    def dequeue(self, queue):
        x = queue[-1]
        queue.pop(0)
        return x

    def breadth_first_transversal(self, start_vertex):
        """"
        connected_components = [start_vertex]
        queue_of_visited_vertices = []
        visited_vertices = []
        for i in range(self.__service_graph.get_number_of_vertices()):
            visited_vertices.append(False)
        visited_vertices[start_vertex] = True
        self.enqueue(queue_of_visited_vertices, start_vertex)
        while len(queue_of_visited_vertices) > 0:
            vertex_in_work = self.dequeue(queue_of_visited_vertices)
            for successor in self.__service_graph.get_successors()[vertex_in_work]:
                if not visited_vertices[successor]:
                    self.enqueue(queue_of_visited_vertices, successor)
                    visited_vertices[successor] = True
                    connected_components.append(successor)
            #for predecessor in self.__service_graph.get_predecessors()[vertex_in_work]:
                #if not visited_vertices[predecessor]:
                    #self.enqueue(queue_of_visited_vertices, predecessor)
                    #visited_vertices[predecessor] = True
                    #connected_components.append(predecessor)
        return connected_components
        """

    def service_get_edges(self):
        return self.__service_graph.get_edges()

    def bfs_connected_components(self):
        visited = set()
        components = []
        for vertex in self.__service_graph.get_vertices():
            if vertex not in visited:
                component = set()
                queue = deque([vertex])
                while queue:
                    current_vertex = queue.popleft()
                    if current_vertex not in visited:
                        visited.add(current_vertex)
                        component.add(current_vertex)
                        for successor in self.__service_graph.get_successors()[current_vertex]:
                            if successor not in visited:
                                queue.append(successor)
                        for predecessor in self.__service_graph.get_predecessors()[current_vertex]:
                            if predecessor not in visited:
                                queue.append(predecessor)
                components.append(component)
        return components

    def dijkstra_good(self, source, target):

        cost = {vertex: inf for vertex in self.__service_graph.get_vertices()}
        cost[source] = 0

        visited = set()

        heap = []
        heappush(heap, (0, source))

        previous = {}

        while heap:
            current_cost, current_vertex = heappop(heap)

            if current_vertex == target:
                path = [target]
                while path[-1] != source:
                    path.append(previous[path[-1]])
                path.reverse()
                return current_cost, path

            visited.add(current_vertex)

            for neighbor in self.__service_graph.get_successors()[current_vertex]:
                if neighbor not in visited:
                    new_cost = current_cost + self.__service_graph.get_edge_cost(current_vertex, neighbor)
                    if new_cost < cost[neighbor]:
                        cost[neighbor] = new_cost
                        heappush(heap, (new_cost, neighbor))
                        previous[neighbor] = current_vertex

        return None, None

    def verify_dag(self):
        in_degree = [0] * self.__service_graph.get_number_of_vertices()
        queue = deque()

        for vertex in self.__service_graph.get_vertices():
            for successor in self.__service_graph.get_successors()[vertex]:
                in_degree[successor] += 1

        for vertex in self.__service_graph.get_vertices():
            if in_degree[vertex] == 0:
                queue.append(vertex)

        visited = 0
        while queue:
            vertex = queue.popleft()
            visited += 1

            for successor in self.__service_graph.get_successors()[vertex]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)

        return visited == self.__service_graph.get_number_of_vertices()

    def topological_sort(self):
        in_degree = [0] * self.__service_graph.get_number_of_vertices()
        sorted_order = []
        queue = deque()

        for vertex in self.__service_graph.get_vertices():
            for successor in self.__service_graph.get_successors()[vertex]:
                in_degree[successor] += 1

        for vertex in self.__service_graph.get_vertices():
            if in_degree[vertex] == 0:
                queue.append(vertex)

        while queue:
            vertex = queue.pop()
            sorted_order.append(vertex)

            for successor in self.__service_graph.get_successors()[vertex]:
                in_degree[successor] -= 1
                if in_degree[successor] == 0:
                    queue.append(successor)

        if len(sorted_order) != self.__service_graph.get_number_of_vertices():
            return []

        return sorted_order

    def highest_cost_path(self, start, end):
        topological_order = self.topological_sort()
        distance = [float('-inf')] * self.__service_graph.get_number_of_vertices()
        distance[start] = 0

        for node in topological_order:
            if node == end:
                break
            for neighbor in self.__service_graph.get_successors()[node]:
                new_distance = distance[node] + self.__service_graph.get_edge_cost(node, neighbor)
                distance[neighbor] = max(distance[neighbor], new_distance)

        return distance[end]
