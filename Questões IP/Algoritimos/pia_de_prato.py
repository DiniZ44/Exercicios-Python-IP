def cadastrar_louca(pilha):
    
    louca = input("Nome da peça que será colocada na pia: ")
    pilha.append(louca)
    
    print("A peça %s foi colocada na pia com sucesso!" % louca)
    
    print("\n")
    
    return pilha

def lavar_louca(pilha):
    
    if len(pilha) > 0:
        louca = pilha.pop(len(pilha)-1)
        print("A peça %s foi lavada com sucesso." % louca)
    else:
        print("A pia está limpa.")
    
    print("\n")
    
    return pilha

def mostrar_pilha(pilha):
    print(" ==== PIA DE PRATOS ==== ")
    if len(pilha) > 0:
        for i, louca in enumerate(pilha):
            print("[%d] - %s" % (i+1, louca))
    else:
        print("A pia está limpa.")
    
    print("\n")

def principal():
    pilha = []
    while True:
        print(" 1 - Colocar louça na pia")
        print(" 2 - Lavar uma peça")
        print(" 3 - Mostra pia")
        print(" 4 - Sair")
        
        opcao = int(input("> "))
        
        if opcao < 1 or opcao > 4:
            print("Opção inválida")
        elif opcao == 1:
            pilha = cadastrar_louca(pilha)
        elif opcao == 2:
            pilha = lavar_louca(pilha)
        elif opcao == 3:
            mostrar_pilha(pilha)
        else:
            print("Saindo do programa...")
            break
        

principal()
    