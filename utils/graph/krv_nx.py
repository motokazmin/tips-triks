import networkx as nx

def remove_betweenness_centrality(g, threlshold = 0.01):
  c = nx.betweenness_centrality(g)
  d = dict(filter(lambda elem: elem[1] > threlshold, c.items()))
  return nx.Graph(g).remove_nodes_from(d.keys())

