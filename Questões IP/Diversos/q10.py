qnt_idades = 0
soma_idades = 0

print("Calculo de média de idades")
print("Digite quantas idades julgar necessárias")
print("Para encerrar o programa! Digite 0")

while True:
    idade = int(input("Digite sua idade: "))
    
    if idade == 0:
        print("Fim do programa!")
        break
  
    
    else:
        qnt_idades += 1
        soma_idades = idade + soma_idades
        media_idades = soma_idades / qnt_idades
print("A média das idades é de: %.2f"%media_idades)
print("Obrigado! Pela preferência")
        
    
    