from dgnx.classes import *
import pickle

dyn = DynamicDirectedGraph()

for v in range(10000):
    dyn.add_delta(v, 1, v, weight=2)

dyn.compute_evenly_distributed_snapshots(2)

with open("test.txt",'wb') as outfile:
    pickle.dump(dyn, outfile)
