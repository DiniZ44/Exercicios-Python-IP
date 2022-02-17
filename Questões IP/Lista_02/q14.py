salario = float(input("Digite seu salário: "))

if salario <= 500:
    aumento = salario*(5/100)
    print("Bônus de R$%.2f" %aumento)
elif salario > 500  and salario < 1200:
    aumento = salario*(12/100)
    print("Bônus de R$%.2f" %aumento)
    
    if salario <= 600 :
        bonus = 150
        print("Parabéns! Ganhou o auxilio escola de R$ %.2f"%bonus)
    
    else:
        bonus = 100
        print("Parabéns! Ganhou o auxilio escola de R$ %.2f"%bonus)

else:
    print("Sem bonificações disponiveis!")
    