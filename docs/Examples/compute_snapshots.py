from dgnx.classes import *

dyn = DynamicDirectedGraph()

for v in range(10000):
    dyn.add_delta(v, 1, v, weight=2)

dyn.compute_evenly_distributed_snapshots(10, png=True)
