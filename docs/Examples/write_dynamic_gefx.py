from dgnx.classes import *
import networkx as nx

#TODO

dyn = DynamicDirectedGraph()

for v in range(10000):
    dyn.add_delta(v, 1, v, weight=2)

dyn.compute_snapshot(10000)
nx.write_gexf(dyn.current_state['state'], "test.gexf")