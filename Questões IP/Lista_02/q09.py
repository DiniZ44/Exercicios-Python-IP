salario = float(input("Digite seu salário: "))

if salario < 500:
    aumento = salario *(30/100)
    novo_salario = aumento + salario
    print("O seu aumento salarial é de R$ %.2f"%aumento)
    print("Novo saldo disponivel é R$ %.2f"%novo_salario)
else: 
    print("Desculpe! O reajuste salarial não está disponivel")