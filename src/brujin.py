class Nodo:
    def __init__(self, prox=None, ant=None, p1=None, p2=None):
        self.prox = prox
        self.ant = ant
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        info = ''.join(self.p1)
        info += " e " + ''.join(self.p2)
        return info


def paired_composition(sequencia, k):
    n_pulos = len(sequencia) - (2 * k)

    no = Nodo()

    for i in range(n_pulos + 1):
        trecho = sequencia[i:i + ((2 * k) + 1)]
        parte1 = trecho[:k]
        parte2 = trecho[k + 1:]

        meio = int(k / 2)
        if k % 2 == 1:  # caso seja ímpar
            meio += 1

        no.p1 = parte1[:meio]
        no.p2 = parte2[:meio]

        print(no)


def imprimir_nos(no):
    while no:
        print(no)
        no = no.prox


def main():
    # no1 = Nodo(21)
    # no2 = Nodo(12)
    # no3 = Nodo(23)
    # no1.prox = no2
    # no2.prox = no3
    #
    # imprimir_nos(no1)

    sequencia = 'TAATGCCATGGGATGTT'
    k = 3
    paired_composition(sequencia, k)


if __name__ == '__main__':
    main()
