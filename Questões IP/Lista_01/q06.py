salario_base = float(input("Digite seu salario básico: "))

grat = (salario_base * 5/100) + salario_base
imposto = grat * (7/100)

print("Sua gratificação é de:R$ %.2f e imposto a ser cobrado:R$ %.2f" % (grat, imposto))
