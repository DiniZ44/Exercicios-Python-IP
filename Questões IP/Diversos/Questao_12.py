LINHAS = 2  # dimensão 1
COLUNAS = 2  # dimensão 2

matriz = []

nome_loja = []
nome_produto = []
selecionados = []


while len(nome_loja) < 8:

    nome = input("Digite o nome da Loja: ")
    nome_loja.append(nome)

    i = 0
    while i < LINHAS:
        matriz.append([])
        j = 0
        while j < COLUNAS:
            produto = input("Digite o nome do Produto: ")
            nome_produto.append(produto)


            valor = float(input("Digite o preco do produto: (%dx%d): " % (i, j)))
            matriz[i].append(valor)

            if valor <= 120:
                x = (nome,produto,valor) # Uma tupla, poderia ser uma lista ou dicionario
                #pra salvar o nome da loja ... se o preço for menor que 120
                selecionados.append(x) #selecionados sera um lista de tulpas no caso
            j += 1
        i += 1

print(matriz)
for i in selecionados:
    print("\nLoja: %s\nProduto: %s\nPreco: %.2f\n"%(i[0],i[1],i[2]))
