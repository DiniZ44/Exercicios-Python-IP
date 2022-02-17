salario = float(input("Digite seu salário: "))
kw = float(input("Digite a quantidade e quilowatts consumido : "))

valor_kw = (salario/5)*kw
valor_total = valor_kw * kw
valor_desconto = valor_total - (valor_total * (15/100)) 

print("########################################")
print("              NOTA FISCAL               ")
print("########################################")
print("     29/05/2017  13:06  Nº 17450        ")
print("########################################")
print("CLIENTE: JOÃO DO NASCIMENTO FILHO SOARES")
print("078 875 356 057")
print("########################################")
print("Preço por quilowatts é de R$ %.2f" %valor_kw)
print("########################################")
print("Valor:  R$ %.2f" %valor_total )
print("########################################")
print("Desconto adquirido: 15%")
print("########################################")
print("########################################")
print("Total:  R$ %.2f" %valor_desconto)
print("########################################")
print("                  Vencimento: 12/06/2017")
print("########################################")
print("########################################")
print("Obrigado pela preferência")


