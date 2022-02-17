salario = float(input("Digite seu salário: "))
perc_aumento = float(input("Digite o percenteual de aumento: "))

aumento = salario * (perc_aumento/100)
resultado = aumento + salario

print("Seu novo salario é de:R$ %.2f, aumento: R$ %.2f" % (resultado, aumento))



