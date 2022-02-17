print("Menu de opções:")
print("1. Imposto.")
print("2. Novo salário.")
print("3. Classificação.")
opcao = int(input(">"))

if  opcao == 1:
    salario = float(input("Digite seu salário: "))
    if salario >= 500 :
        imposto = salario * (5/100)
        print("O imposto a ser pago é de R$ %.2f"%imposto)
    elif salario < 500 and salario > 850 :
        imposto = salario * (10/100)
        print("O imposto a ser pago é de R$ %.2f"%imposto)
    else :
        imposto = salario * (15/100)
        print("O imposto a ser pago é de R$ %.2f"%imposto)
        
elif opcao == 2:
    salario = float(input("Digite seu salário: "))
    if salario <= 1500 :
        aumento = salario + 25
        print("Seu novo salário é de R$ %.2f"%aumento)
    elif salario < 750 and salario > 1500 :
        aumento = salario + 50
        print("Seu novo salário é de R$ %.2f"%aumento)
    elif salario < 450 and salario > 749.99 :
        aumento = salario + 75
        print("Seu novo salário é de R$ %.2f"%aumento)
    else:
        aumento = salario + 100
        print("Seu novo salário é de R$ %.2f"%aumento)
        
elif opcao == 3:
    salario = float(input("Digite seu salário: "))
    if salario > 700 :
        print("Mal remunerado!")
    else:
        print("Bem remunerado!")
else: 
    print("Apenas opções acima são aceitas")