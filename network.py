import collections
import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np

N=8

G = nx.gnp_random_graph(N, 0.15)
degree_sequence = sorted([d for n, d in G.degree().items()])
degreeCount = collections.Counter(degree_sequence)
deg ,cnt  =zip(*degreeCount.items())
fig, ax = plt.subplots()
plt.bar(deg,cnt,width=0.8,color = "b")
plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
plt.axes([0.4, 0.4, 0.5, 0.5])
Gcc = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)[0]
pos = nx.spring_layout(G)
plt.axis('off')
nx.draw_networkx_nodes(G, pos, node_size=20)
nx.draw_networkx_edges(G, pos, alpha=0.4)
nx.draw_networkx(G,pos,with_labels=True)
plt.show()




#calculate path lenght to the nearest influencer and inflencer node.
par = 0.7 # upper 100*(1-par)%
hub = [n for n, d in G.degree().items() if d>max(degreeCount.keys())*par]
print("hub:{}".format(hub))
store = [] # [influencer node, path length to influencer]
isolates = nx.isolates(G)
l1 = []
l2 = []
# find nodes which have no path to hub.
sub=[]
for n in range(N):
    ns = nx.node_connected_component(G,n)
    if not ns & set(hub):sub.append(n)
print ("sub",sub)
print("isolates",isolates)
kk = []
for n in G.degree().keys():
    if n in hub or n in isolates or n in sub:
        store.append([n,0])
    else:
        for x in hub:
            kk.append(nx.shortest_path_length(G,n,x))
        mi = min(kk)
        store.append([hub[kk.index(mi)],mi])
        kk.clear()
num = [i for i in range(N)]
di = dict(zip(num,store)) # di = {node num:[nearest influencer, path length to nearest influencer]}
di
