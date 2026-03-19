import networkx as nx
import pandas as pd

class GraphService:

    def __init__(self, file_path="data/network_logs.csv"):
        self.df = pd.read_csv(file_path)
        self.graph = nx.from_pandas_edgelist(self.df, "src_ip", "dst_ip")

    def get_graph(self):
        return self.graph

    def get_nodes(self):
        return list(self.graph.nodes())

    def get_neighbors(self, node):
        return list(self.graph.neighbors(node))