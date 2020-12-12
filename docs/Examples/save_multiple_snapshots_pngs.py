from dgnx.classes import *
import networkx as nx

dyn = DynamicDirectedGraph()


for v in range(10000):
    dyn.add_delta(v, 1, v, weight=2)


print("\n")

dyn.compute_snapshot(2)
print(dyn.current_state['t'])
print(dyn.current_state['state'].nodes())
print(dyn.current_state['state'].edges())
dyn.save_current_state_png()
print("\n")

dyn.compute_snapshot(5)
print(dyn.current_state['t'])
print(dyn.current_state['state'].nodes())
print(dyn.current_state['state'].edges())
dyn.save_current_state_png()


print("\n")

dyn.compute_snapshot(3)
print(dyn.current_state['t'])
print(dyn.current_state['state'].nodes())
print(dyn.current_state['state'].edges())
dyn.save_current_state_png()

print("\n")

dyn.compute_snapshot(7)
print(dyn.current_state['t'])
print(dyn.current_state['state'].nodes())
print(dyn.current_state['state'].edges())
dyn.save_current_state_png()

print("\n")

dyn.compute_snapshot(3)
print(dyn.current_state['t'])
print(dyn.current_state['state'].nodes())
print(dyn.current_state['state'].edges())
print("\n")

dyn.compute_snapshot(10000)
print(dyn.current_state['t'])
print(dyn.current_state['state'].nodes())
print(dyn.current_state['state'].edges())
dyn.save_current_state_png()
