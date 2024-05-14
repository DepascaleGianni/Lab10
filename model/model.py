import networkx as nx
from database.DAO import DAO


class Model:

    def __init__(self):
        self._all_countries = DAO.get_all_countries()
        self._sol_graph = nx.Graph()
        self.countries_map = {}
        for c in self._all_countries:
            self.countries_map[c.CCode] = c


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

    def number_conn_comp(self):
         return len(list(nx.connected_components(self._sol_graph)))
    def get_num_nodes(self):
        return self._sol_graph.number_of_nodes()

    def get_num_edges(self):
        return self._sol_graph.number_of_edges()

    def get_countries(self):
        return self._all_countries