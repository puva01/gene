import random
import numpy as np
import networkx as nx
%matplotlib inline
N=10

mat = np.random.randint(0,2,(N,N))
mat_symm= np.triu(mat,k=1) + np.triu(mat.T,k=1).T

gene = []
def create_gene(array):
    for i in range(N):
        tmp = array[i,i+1:]
        gene.extend(tmp)
    return gene

#create Graph based on gene
nodes = [i for i in range(N)]
G = nx.from_numpy_matrix(mat_symm)
G.add_nodes_from(nodes)
nx.draw_networkx(G,with_labels=True)
plt.axis("off")
plt.show()
