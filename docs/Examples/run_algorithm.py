from dgnx.algorithms import *
import random

# Use main for multiprocess operations
if __name__ == '__main__':

    dyn = DynamicDirectedGraph()
    for v in range(0, 10000):
        dyn.add_delta(v, 1, v, weight=2)
        for u in range(random.randint(0,10)):
            dyn.add_delta(v, u, random.randint(0,10000), weight=2)

    b = time.time()
    t1, r1 = compute_snapshots_and_run_algorithm(dyn, 100, 'betweenness_centrality', nprocs=1)
    e = time.time()
    print(e-b)
    t2, r2 = compute_snapshots_and_run_algorithm(dyn, 100, 'betweenness_centrality', nprocs=-1)
    print(t1 == t2)
    print(r1 == r2)
    #print("T1 -> " + str(t1))
    #print("R1 -> " + str(r1))

    #print("T2 -> " + str(t2))
    #print("R2 -> " + str(r2))
    
    end = time.time()
    print(end-e)
