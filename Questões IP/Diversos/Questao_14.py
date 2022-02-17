"""
Em um campeonato de futebol existem cinco times e cada um possui onze jogadores.
Faça um programa que receba a idade, o peso e a altura de cada um dos jogadores, calcule e
mostre:
• A quantidade de jogadores com idade inferior a 18 anos;
• A média das idades dos jogadores de cada time;
• A média das alturas de todos os jogadores do campeonato; e
• A porcentagem de jogadores com mais de 80 kg entre todos os jogadores do
campeonato.

"""

qtd_times = 15
qtd_jogadores_por_time = 5

cont_menor_18 = 0

soma_altura_geral = 0


jogadores_maiores_de_80kg = 0
qtd_maiores_de_80kg = 0

lista = [] # lista para tds os times
lista_idade_media_por_time = []


for x in range(qtd_times):

    time = [] # reinicia  os dados do time, apos cada saida do while
    soma_idade_por_time = 0 # reinicia  os dados da idade , apos cada saida do while

    while len(time) < qtd_jogadores_por_time  and x < qtd_times:
        print("--- Time %d ---" %(x+1))
        print("Jogador %d" %(len(time)+1))

        idade = int(input("digite a Idade: "))
        soma_idade_por_time += idade
        if idade < 18:
            cont_menor_18+=1

        peso = float(input("Digite o peso: "))
        if peso >= 80: # se o peso for maior que 80kg, aumenta o contador abaixo
            qtd_maiores_de_80kg +=1

        altura = float(input("Digite a altura: "))
        soma_altura_geral+=altura # a soma das alturas de tds os jogadores do campeonato

        time.append([idade,peso,altura]) # cada novo jogador eh salvo em seu time
    media_idade = soma_idade_por_time / qtd_jogadores_por_time# calcula a media de idade por time

    lista_idade_media_por_time.append(media_idade) #um lista com a idade media dos jogadores de cada time
    lista.append(time)# apos um time esta com tds os jogadores cadastrado, o time eh salvo na lista

qtd_jogadores = qtd_times * qtd_jogadores_por_time


print("Quatidade de jogadores com menos de 18 anos: %d"% cont_menor_18)
for i, x in enumerate (lista_idade_media_por_time):
    print("Media das Idades do time %d: %d"% (i+1,x))
print("A média das alturas de todos os jogadores do campeonato: %.2f" % (soma_altura_geral / qtd_jogadores))
print("A porcentagem de jogadores com mais de 80 kg entre todos os jogadores do campeonato: %.2f"%((qtd_maiores_de_80kg / qtd_jogadores)*100))
