from __future__ import division
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx
import networkx as nx


class Usuarios:
    def __init__(self):
            self.screen_name = str()
            self.listaDeSeguidores = list()
            self.listaDeTweets = list()
            self.citacoes = 0


def contains(u, usuarios):
        j = 0
        for i in usuarios:
            if i.screen_name == u:
                return j
            j = j + 1

        return 0



listaU = []
listaC = []

with open("recentes.txt") as file:
    for line in file:
        l = line.split()
        if line[0]  != "\n":
            listaU.append(l[0])
            listaC.append(l[1])

with open("influentes.txt") as file:
    for line in file:
        l = line.split()
        if listaU.count(line[0])  == 0 and line[0]  != "\n":
            listaU.append(l[0])
            listaC.append(l[1])


usuarios = [Usuarios() for i in range(len(listaU))]

for i in range(len(listaU)): #tira usuarios repetidos da minha lista
        usuarios[i].screen_name = listaU[i]
        usuarios[i].citacoes = listaC[i]

listaS = []
#----------------------------------------------------------------------
G = nx.DiGraph()
for i in usuarios:
    G.add_node(i.screen_name)

with open("seguidorees.txt") as file:
    for line in file:
        l = line.split()
        s = l[1].split(",")
        for i in s:
            #print("1:{} 2 :{}".format(l[0],i))
            G.add_edge(i,l[0])

pos = nx.layout.kamada_kawai_layout(G)
node_sizes = []
for u in usuarios:
    node_sizes.append(10*(int(u.citacoes)+1))

nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="gray",alpha=0.9)
label = nx.draw_networkx_labels(G, pos,font_size=10,font_family= "Arial",font_color="Red")
edges = nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=15 , width=2,edge_color="black")

ax = plt.gca()
ax.set_axis_off()
# plt.savefig("Graph.png", format="PNG")
plt.show()



print("Numero de Vertices: {}".format(G.number_of_nodes()))
print("Numero de Arestas: {}".format(G.number_of_edges()))
print("Densidade: {}".format(networkx.classes.function.density(G)))
print("È Fortemente Conectado ? {}".format(networkx.algorithms.components.is_strongly_connected(G)))
print("------------------------------------------\n\n")