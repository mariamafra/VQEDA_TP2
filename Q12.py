
class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self._hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):  
          if k == chave:
              self.tabela[indice][i] = (chave, valor)
              return
        self.tabela[indice].append((chave, valor))


    def buscar(self, chave):
        indice = self._hash(chave)
        for k, v in self.tabela[indice]:
            if k == chave:
                return v
        return None

    def remover(self, chave):
        indice = self._hash(chave)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == chave:
                del self.tabela[indice][i]
                return
        return None



tabela = TabelaHash(10)
tabela.inserir("maçã", 1)
tabela.inserir("banana", 2)
tabela.inserir("cereja", 3)
tabela.inserir("maçã", 4)


print(tabela.buscar("banana"))
print(tabela.buscar("uva")) 
print(tabela.buscar("maçã")) 


tabela.remover("banana")
print(tabela.buscar("banana"))



