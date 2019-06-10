import random


class Bio(object):
    @staticmethod
    def criar_kmer_random(k):
        """
        Retorna uma sequencia(kmer) aleatória de tamanho k
        :param k: tamanho (length) do kmer desejado.
        :rtype: list()
        :return lista de sequencia aleatoria
        """
        conjunto = "ACTG"
        kmer = ''.join(random.choice(conjunto) for i in range(k))
        return kmer

    @staticmethod
    def calcular_erros(trecho, kmer, k):
        """
        Calcula a quantidade de erros (mutações) de um trecho em relação a
        sequencia original de tamanho k
        :param trecho:
        :param kmer:
        :param k:
        :return:
        """

        erros = 0
        for i in range(k):
            if trecho[i] != kmer[i]:
                erros += 1
        return erros

    def percorrer(self, kmer, trecho, k):
        """
        Slice and switch
        Percorre o kmer original
        :param kmer:
        :param trecho:
        :param k:
        :return:
        """
        erros = []
        n_pulos = len(kmer) - k + 1

        for i in range(n_pulos):
            comparador = kmer[i:i + k]
            erros.append(self.calcular_erros(trecho, comparador, k))

        return erros

    def calcular_distancia(self, kmer, k):
        trecho = list(self.criar_kmer_random(k))
        distancia = min(self.percorrer(trecho, kmer, k))

        return distancia

    def criar_motif_random(self, linha, coluna):
        """
        Cria o motif (matriz contendo várias sequencias aleatórias de motif).
        :param linha:
        :param coluna:
        :return:
        """

        motif = []

        for i in range(linha):
            kmer = self.criar_kmer_random(coluna)
            motif.append(kmer)

        return motif

    @staticmethod
    def profile_sequencia(motif):
        """
        Calcula a frequencia e cria o profile (matriz com a criar_frequencia),
        retornando-o. O padrao de visualizacao é ACGT
        :param motif: a matriz de motif
        :return: matriz contendo a frequencia absoluta
        """

        linhas = len(motif)
        colunas = len(motif[0])
        profile = [[], [], [], []]

        # zerando o profile
        for i in range(4):
            for j in range(colunas):
                profile[i].append(0)

        for i in range(colunas):
            for j in range(linhas):
                if motif[j][i] == 'A':
                    profile[0][i] += 1

                elif motif[j][i] == 'C':
                    profile[1][i] += 1

                elif motif[j][i] == 'G':
                    profile[2][i] += 1

                elif motif[j][i] == 'T':
                    profile[3][i] += 1

        return profile
