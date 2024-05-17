import copy

import networkx as nx
from database.DAO import DAO
from model.country import Country


class Model:

    def __init__(self):
        self._all_countries = DAO.get_all_countries()
        self._sol_graph = nx.Graph()
        self.countries_map = {}
        for c in self._all_countries:
            self.countries_map[c.CCode] = c
        self.reachable_recursion_graph = nx.Graph()


    def build_graph(self, year):
        self._sol_graph.clear()
        self.add_nodes(year)
        self.add_edges(year)

    def add_nodes(self,year):
        sel_nodes = DAO.get_sel_countries(year)
        for c in sel_nodes:
            self._sol_graph.add_node(self.countries_map[c])

    def add_edges(self,year):
        self._sol_graph.clear_edges()
        all_conn = DAO.get_all_connection(year)
        for c in all_conn:
            self._sol_graph.add_edge(self.countries_map[c.state1no],self.countries_map[c.state2no])

    def printable_graph(self):
        result = []
        for el in self._sol_graph.degree:
            result.append(el)
        return result

    def get_BFS_nodes(self, source):
        edges = nx.bfs_edges(self._sol_graph,source)
        visited = []
        for u,v in edges:
            visited.append(v)
        return visited

    def get_DFS_nodes(self, source):
        edges = nx.dfs_edges(self._sol_graph, source=source)
        visited = []
        for u, v in edges:
            visited.append(v)
        return visited

    def get_reachable_recursion(self,source):
        self.reachable_recursion_graph.clear()
        self.recursion(source, available=list(self._sol_graph.nodes))
        return list(self.reachable_recursion_graph.nodes)

    def recursion(self,source, available : list[Country]) :
        #condizione terminale : non ho più nodi in cui andare
        #if .....
        if len(list(self.reachable_recursion_graph.nodes)) == 0:
            self.reachable_recursion_graph.add_node(source)
            available.remove(source)
            self.recursion(source,available)
        else:
            for v in available:
                if self._sol_graph.has_edge(source,v):
                    self.reachable_recursion_graph.add_edge(source,v)
                    available.remove(v)
                    self.recursion(v, available)


    def number_conn_comp(self):
         return len(list(nx.connected_components(self._sol_graph)))
    def get_num_nodes(self):
        return self._sol_graph.number_of_nodes()

    def get_num_edges(self):
        return self._sol_graph.number_of_edges()

    def get_countries(self):
        return self._all_countries