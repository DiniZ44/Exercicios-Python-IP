LINHAS = 3 #produtos
COLUNAS = 3 #lojas

#precos = [[12.5, 18.2, 7.5], [7.5, 10.3, 5.7], [50.35, 65.0, 48.3]]
#custos = [4.0, 2.5, 10.3]

#criando a matriz precos
precos = []
i = 0
while i < LINHAS:
    precos.append([]) #cadastrando a linha i
    j = 0
    while j < COLUNAS:
        valor = float(input("Digite o valor do produto %d na loja %d:" % (i, j)))
        precos[i].append(valor)
        j += 1
    i += 1

#criando o vetor custos
i = 0
custos = []
while i < LINHAS:
    frete = float(input("Digite o frete do produto %d: " % i))
    custos.append(frete)
    i += 1

impostos = []
#calculando o valor do imposto para cada produto em cada loja
for i, linha in enumerate(precos):
    
    impostos.append([])
    for j, coluna in enumerate(linha):
        
        produto_atual = coluna
        
        if produto_atual < 500.0:
            imposto = produto_atual * (5/100)
        elif produto_atual >= 500.0 and produto_atual <= 1000.0:
            imposto = produto_atual * (10/100)
        else:
            imposto = produto_atual * (20/100)
        
        impostos[i].append(imposto)

#gerando o relatório
for i, linha in enumerate(precos):
    print("Produto: %d" % i)
    print("Frete do produto %d: %.2f" % (i, custos[i]))
    for j, coluna in enumerate(linha):
        print("Na loja %d: " % j)
        print("\tO imposto desse produto é: R$%.2f" % impostos[i][j])
        print("\tO preço desse produto é: R$%.2f" % precos[i][j])
        preco_final = precos[i][j] + impostos[i][j] + custos[i]
        print("\tO preço FINAL desse produto é: R$%.2f" % preco_final)
    print("====\n")
        
