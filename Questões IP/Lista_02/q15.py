preco_atual = float(input("Digite o preço atual do produto: "))
venda_mensal = float(input("Digite a venda mensal: "))

if venda_mensal < 500:
    if preco_atual < 30:
        aumento = preco_atual * (10/100) + preco_atual
        print("O novo preço do produto é R$ %.2f" % aumento)
    else :
        print("O preço seá mantido.")
        
elif venda_mensal >= 500 and venda_mensal < 1200:
    if preco_atual >= 30 and preco_atual <80:
        aumento = preco_atual * (15/100) + preco_atual
        print("O novo preço do produto é R$ %.2f" % aumento)
    else :
        print("O preço seá mantido.")
    
else:
    if preco_atual >= 80:
        aumento = preco_atual * (20/100) - preco_atual
        print("O novo preço do produto é R$ %.2f" % aumento)
    else :
        print("O preço seá mantido.")
    
        
    
            