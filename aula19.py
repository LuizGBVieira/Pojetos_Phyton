def listar(tarefas):
    print()
    if not tarefas:
        print('Não há nenhuma tarefa a listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t {tarefa}')

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Não há nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'A tarefa {tarefa} foi retirada da lista!')
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Não há nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'A tarefa {tarefa} foi recolocada na lista!')
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você nao digitou nenhuma tarefa')
        return
    tarefas.append(tarefa)


tarefas=[]
tarefas_refazer=[]

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite alguma tarefa ou comando:')

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
    else:
        adicionar(tarefa, tarefas)
        continue
