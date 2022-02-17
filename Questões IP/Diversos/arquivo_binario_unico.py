import pickle

def cpf_existe(cpf, funcionarios):
    
    for funcionario in funcionarios:
        if funcionario["cpf"] == cpf:
            return True
    
    return False

def cadastro_funcionario(funcionarios):
    
    #exigindo o cadastro de um CPF inédito
    while True:
        cpf = input("Digite o CPF do funcionário: ")
        
        if cpf_existe(cpf, funcionarios):
            print("Esse CPF não pode ser cadastrado. Pois já existe no sistema.")
            print("Por favor, digite novamente.")
        else:
            break
        
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    
    funcionario = {
            "cpf": cpf,
            "nome": nome,
            "salario": salario
        }
    
    funcionarios.append(funcionario)
    
    print("O funcionário %s foi salvo com sucesso!\n\n" 
                % funcionario["nome"])
    
    return funcionarios

def atualizar_funcionario(funcionarios):
    cpf = input("Digite o CPF: ")
    
    if cpf_existe(cpf, funcionarios):
        
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                print("Nome atual: %s" % funcionario["nome"])
                novo_nome = input("Digite o novo nome do funcionário: ")
                novo_salario = float(input("Digite o novo salário do funcionário: "))
                
                funcionario["nome"] = novo_nome
                funcionario["salario"] = novo_salario
                break
                
    else:
        print("Funcionário não está cadastrado no sistema.")
    
    print("\n")
    
    return funcionarios

def remover_funcionario(funcionarios):
    cpf = input("Digite o CPF: ")
    
    if cpf_existe(cpf, funcionarios):
        
        for i, funcionario in enumerate(funcionarios):
            if funcionario["cpf"] == cpf:
                del funcionarios[i]
                print("O funcionário foi deletado com sucesso!")
                break
                
    else:
        print("Funcionário não está cadastrado no sistema.")
    
    print("\n")
    
    return funcionarios

def buscar_funcionario(funcionarios):
    cpf = input("Digite o CPF: ")
    
    if cpf_existe(cpf, funcionarios):
        
        for i, funcionario in enumerate(funcionarios):
            if funcionario["cpf"] == cpf:
                print("Funcionário %d:" % (i+1))
                print("\tNome: %s" % funcionario["nome"])
                print("\tCPF: %s" % funcionario["cpf"])
                print("\tSalário: %0.2f" % funcionario["salario"])
                break
                
    else:
        print("Funcionário não está cadastrado no sistema.")
    
    print("\n")

def salvar(funcionarios):
    arquivo = open("funcionarios.bin", "wb")
    
    pickle.dump(funcionarios, arquivo)
    
    arquivo.close()

def carregar():
    funcionarios = []
    
    try:
        arquivo = open("funcionarios.bin", "rb")
        
        funcionarios = pickle.load(arquivo)
        
        arquivo.close()
        
    except FileNotFoundError:
        pass
        
    
    return funcionarios

def listar_funcionarios(funcionarios):
    print(" == LISTAR TODOS OS FUNCIONÁRIOS ==")
    
    if len(funcionarios) > 0:
        for i, funcionario in enumerate(funcionarios):
            print("Funcionário %d:" % (i+1))
            print("\tNome: %s" % funcionario["nome"])
            print("\tCPF: %s" % funcionario["cpf"])
            print("\tSalário: %0.2f" % funcionario["salario"])
    else:
        print("Não tem nenhum funcionário cadastrado no sistema.")
    
    print("\n")

def folha_salario_mensal(funcionarios):
    
    if len(funcionarios) > 0:
        soma_salarios = 0
        
        for funcionario in funcionarios:
            soma_salarios += funcionario["salario"]
        
        print("A folha do mês é: R$%0.2f" % soma_salarios)
    else:
        print("Não tem gastos com folha salárial.")
    
    print("\n")

def folha_salario_anual(funcionarios):
    
    if len(funcionarios) > 0:
        soma_salarios = 0
        
        for funcionario in funcionarios:
            soma_salarios += funcionario["salario"]
        
        print("A folha do ano é: R$%0.2f" % (soma_salarios*12))
    else:
        print("Não tem gastos com folha salárial.")
    
    print("\n")

def principal():
    funcionarios = carregar()
    
    while True:
        print(" ==== GERENCIAMENTO DE FUNCIONÁRIOS v0.2 ====")
        print(" 1 - Cadastrar funcionário")
        print(" 2 - Atualizar funcionário")
        print(" 3 - Remover funcionário")
        print(" 4 - Buscar funcionário")
        print(" 5 - Listar todos os funcionários")
        print(" 6 - Apresentar a folha salarial do mês")
        print(" 7 - Apresentar a folha salarial do ano")
        print(" 8 - Sair")
        
        opcao = int(input("> "))
        
        if opcao < 1 or opcao > 8:
            print("Opção inválida. Por favor, tente novamente.\n\n")
            continue
        elif opcao == 1:
            funcionarios = cadastro_funcionario(funcionarios)
            salvar(funcionarios)
        elif opcao == 2:
            funcionarios = atualizar_funcionario(funcionarios)
            salvar(funcionarios)
        elif opcao == 3:
            funcionarios = remover_funcionario(funcionarios)
            salvar(funcionarios)
        elif opcao == 4:
            buscar_funcionario(funcionarios)
        elif opcao == 5:
            listar_funcionarios(funcionarios)
        elif opcao == 6:
            folha_salario_mensal(funcionarios)
        elif opcao == 7:
            folha_salario_anual(funcionarios)
        else:
            print("Saindo do programa...\n\n")
            break
    

principal()