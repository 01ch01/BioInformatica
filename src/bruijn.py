class Nodo:
    def __init__(self, item=None):
        """
        Nó que contém dois pares de bases nitrogenadas.
        :param item:
        """
        self.item = item

    def __str__(self):
        return self.item

    def mostrar(self):
        return self.item


def paired_composition(sequencia, k):
    """

    :param sequencia:
    :param k:
    :return:
    """
    n_pulos = len(sequencia) - (2 * k)

    lista_vertices = []
    lista_arestas = []

    for i in range(n_pulos + 1):

        # instanciando novo nodo que será adicionado logo mais
        no = Nodo()

        # primeiro par + letra de intervalo + segundo par
        trecho = sequencia[i: i + (2 * k + 1)]
        parte1 = trecho[:k]
        parte2 = trecho[k + 1:]

        meio = int(k / 2)
        if k % 2 == 1:  # caso k seja ímpar, arredondar o meio pra cima
            meio += 1

        resultado = parte1[:meio] + parte2[:meio]
        # print(resultado)
        no.item = resultado

        # inserindo nó na lista de vértices
        lista_vertices.append(no.item)

        if i == 0:
            pass
        else:
            # criando tupla de ligação do nó anterior com o nó atual
            ligacao = (lista_vertices[i - 1], no.item)

            # inserindo tupla na lista de arestas
            lista_arestas.append(ligacao)

    return [lista_vertices, lista_arestas]


def criar_grafo(lista_vertices, lista_arestas):
    """
    Cria o grafo no formato de lista de adjacência.
    :param lista_vertices: a lista que contém os nós, as 'bolinhas' do grafo
    :param lista_arestas: uma lista que contém várias tuplas. Cada tupla representa uma ligação de um nó com outro.
    :return: um grafo no formato de dicionário, onde cada chave representa um elemento da lista de vértices (nó), e cada
     valor é uma lista de tuplas representando a ligação
    """
    grafo = {}

    for vertice in lista_vertices:
        grafo[vertice] = []
    for aresta in lista_arestas:
        grafo[aresta[0]].append(aresta[1])

    return grafo


def imprimir_nodos(no):
    while no:
        print(no)
        no = no.prox


def main():
    sequencia = 'TAATGCCATGGGATGTT'
    k = 3

    resultado = paired_composition(sequencia, k)

    lista_vertices = resultado[0]
    lista_arestas = resultado[1]

    grafo = criar_grafo(lista_vertices, lista_arestas)

    print("\nAresta   Vértices\n")
    for a, v in grafo.items():
        print(f"{a} ->  {v}")


if __name__ == '__main__':
    main()
