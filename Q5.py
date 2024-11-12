def tarefa_no_topo(pilha_de_tarefas):
    if len(pilha_de_tarefas) > 0:
        return pilha_de_tarefas[-1]
    else:
        return None

pilha_de_tarefas = ['Fazer comida', 'Lavar louça', 'Fazer a cama']
print(tarefa_no_topo(pilha_de_tarefas))