preco = float(input("Digite o preço de fábrica de seu veiculo: "))
lucro_distribuidor = float(input("Digite o percentual do lucro do destribuidor: "))
imposto = float(input("Digite o percentual de impostos: "))
perc_lucro = (lucro_distribuidor/100)
perc_imposto = (imposto/100)

lc_dis = preco*perc_lucro
lc_imp = preco*perc_imposto
preco_final = lc_dis + lc_imp + preco

print("O valor correspondente ao lucro do destribuidor é R$ %.2f, ao imposto é R$ %.2f" % (lc_dis, lc_imp,))
print("O preço do carro para o consumidor sai por R$ %.2f" % preco_final)
