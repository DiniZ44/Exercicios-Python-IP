FILA_MAX = 5
FILA_ATUAL = 0

fila = []

def cadastrar_paciente():
    global FILA_ATUAL
    if FILA_ATUAL < FILA_MAX:
        global fila #permitir que fila seja alterada
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        
        paciente = {"nome": nome, "idade": idade}
        
        if idade < 65:
            #NÃO paciente prioritario
            fila.append(paciente)
            posicao_inserida = FILA_ATUAL + 1
        else:
            #paciente prioritario
            for i, elemento in enumerate(fila):
                if elemento["idade"] >= 65:
                    continue
                
                fila.insert(i, paciente)
                posicao_inserida = i+1
                
                break
        
        FILA_ATUAL += 1
        print("%s foi cadastrado com sucesso na posição %d da fila."
                    % (nome, posicao_inserida))
    else:
        print("A fila está cheia. Paciente não foi cadastrado.")
    
    print("\n")
    
def atender_paciente():
    global FILA_ATUAL
    
    if FILA_ATUAL > 0:
        global fila
        
        paciente = fila.pop(0)
        FILA_ATUAL -= 1
        
        print("O paciente %s foi atendido." % paciente["nome"])
         
    else:
        print("Não tem nenhum paciente na fila. Ninguém foi atendido.")
    
    print("\n")

def mostrar_fila():
    print(" ==== MOSTRAR FILA ==== ")
    if FILA_ATUAL > 0:
        for i, paciente in enumerate(fila):
            print(" [%d] - %s - %d anos" 
                  % (i+1, paciente["nome"], paciente["idade"]))
    else:
        print(" A fila está vazia.")
    
    print("\n")

while True:
    print(" 1 - Cadastrar paciente na fila")
    print(" 2 - Atender paciente da fila")
    print(" 3 - Mostrar fila")
    print(" 4 - Sair")
    opcao = int(input("> "))
    
    if opcao < 1 or opcao > 4:
        print("Opção inválida, por favor, tente novamente!")
        continue
    elif opcao == 1:
        cadastrar_paciente()
    elif opcao == 2:
        atender_paciente()
    elif opcao == 3:
        mostrar_fila()
    elif opcao == 4:
        print("Saindo do programa")
        break
