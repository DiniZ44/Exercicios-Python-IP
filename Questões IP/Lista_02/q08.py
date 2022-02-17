print("Bom dia!")
codigo = int(input("Por favor digite seu código:"))

if codigo <= 5 and codigo > 0:
    salario = float(input("Digite seu salário: "))
    if codigo == 1:
        print("Bom dia! Senhor Escriturário.")
        aumento = (salario * (50/100)) + salario
        print("Seu novo salário é de: %.2f" %aumento)
    elif codigo == 2:
        print("Bom dia! Senhor Secrerário.")
        aumento = (salario * (35/100)) + salario
        print("Seu novo salário é de: %.2f" %aumento)
    elif codigo == 3:
        print("Bom dia! Atendente caixa.")
        aumento = (salario * (20/100)) + salario
        print("Seu novo salário é de: %.2f" %aumento)
    elif codigo == 4:
        print("Bom dia! Senhor Gerente.")
        aumento = (salario * (20/100)) + salario
        print("Seu novo salário é de: %.2f" %aumento)
    else:
        print("Bom dia! Senhor Diretor")
        print("Infelizmente o senhor não possui aumento disponivel!")
      
else:
    print("Erro!")
    print("Você não é cadastrado no sistema")