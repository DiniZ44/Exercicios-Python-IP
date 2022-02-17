salario_base = float(input("Digite seu salario básico: "))

grat = (salario_base + 50)
imposto = grat * (10/100)

print("Sua gratificação é de:R$ %.2f e imposto a ser cobrado:R$ %.2f" % (grat, imposto))
