class FilaAtendimento:
    def __init__(self):
        self.fila = []

    def adicionar_cliente(self, nome):
        self.fila.append(nome)
        print(f"{nome} adicionado à fila.")

    def atender_cliente(self):
        if self.fila:
            nome = self.fila.pop(0)  
            print(f"Atendendo {nome}.")
            return nome
        else:
            print("Fila vazia.")
            return None

    def tamanho_fila(self):
        return len(self.fila)