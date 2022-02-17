´-dep = float(input("Insira o valor de seu depósito: "))
taxa_juros = float(input("Insira o valor da taxa de juros: "))

resultado = dep * (taxa_juros/100)
total = resultado + dep

print("O rendimento mensal foi de R$ %.2f, seu novo saldo bancario é de R$ %.2f" % (resultado, total))
