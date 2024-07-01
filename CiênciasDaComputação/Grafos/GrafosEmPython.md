# Grafos em python

Agora eu vou deixar um exemplo de um grafo não direcionado e outro grafo direcionado que eu fiz em Python:

``` Python
import networkx as nx


"""Aqui vou criar uma função que cria um grafo não direcionado, vou adicionar os vértices (ou nós) e vou adicionar as arestas (conexões entre os vertices)"""

def grafoN():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 1)])
    return G

G = grafoN()

print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
print("Nós:", list(G.nodes()))
print("Arestas:", list(G.edges()))
````

O output esperado é:

```
Número de nós: 5
Número de arestas: 6
Nós: [1, 2, 3, 4, 5]
Arestas: [(1, 2), (1, 3), (1, 5), (2, 4), (3, 4), (4, 5)]
```

No exemplo utilizado, definimos um grafo não direcionado com cinco nós e seis arestas, utilizamos a biblioteca NetworkX para acessar informações como o número de nós e arestas, bem como listar os nós e arestas presentes no grafo. Para ilustrar de forma mais clara desenhei este exemplo de como ficaria esse grafo!

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/grafoPython.jpg" alt="Grafo não direcionado em python">

Nesse grafo em especifico os nós (ou vértices) são ilustrados com números para facilitar a sua compreensão. Esses são grafos não direcionados, agora vou falar sobre os grafos direcionados

Os grafos direcionados são utilizados em diversas aplicações práticas, como modelagem de fluxos de informações, redes de transporte, sistemas de navegação, entre outros. A capacidade de representar e analisar relações direcionadas entre elementos torna os grafos direcionados uma ferramenta poderosa para entender a dinâmica de sistemas complexos e orientados por fluxos. Nos grafos direcionados cada aresta possui uma seta indicando a direção do fluxo entre os vértices. Isso reflete a natureza direcional das relações representadas no grafo. Os vértices são dispostos no plano de acordo com as coordenadas e configurações definidas na representação gráfica. A estilização, incluindo cores, tamanhos e fontes, contribui para uma visualização clara da estrutura de rede direcionada. Aqui vou deixar mais um exemplo de um grafo só que dessa vez direcionado:

```Python
import networkx as nx

def grafoD():
    G = nx.DiGraph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 1)])
    return G

G = grafoD()

print("Número de nós:", G.number_of_nodes())
print("Número de arestas:", G.number_of_edges())
print("Nós:", list(G.nodes()))
print("Arestas:", list(G.edges()))
```

Output esperado:

```
Número de nós: 5
Número de arestas: 6
Nós: [1, 2, 3, 4, 5]
Arestas: [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 1)]
```

Vou deixar um exemplo ilustrativo de como é um grafo direcionado abaixo:

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/grafoDir.jpg" alt="Grafo direcionado em python">

Perceba que no grafo direcionado no exemplo acima nós podemos ir do quatro pro cinco, mas não podemos ir diretamente do cinco para o quatro, isso ocorre porquê nós não temos arestas indo do cinco pro quatro, só temos arestas indo do quatro pro cinco. Rotas estabelecidas (1 -> 2), (1 -> 3), (2 -> 4), (3 -> 4), (4 -> 5), (5 -> 1).

Exercicio: faça um exemplo de grafo não direcionado com 8 vértices e 9 arestas
