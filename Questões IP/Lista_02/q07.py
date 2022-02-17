print("Menu de opções:")
print("1.Somar dois números.")
print("2.Raiz quadrada de um número.")
    
opcao = int(input("Digite a opção desejada: "))
import math
    
if opcao ==1:
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite outro número:"))
    res = n1 + n2
    print("A soma dos números é: %d"%res)
elif opcao ==2:
    n3 = float(input("Digite um número: "))
    raiz = math.sqrt(n3)
    print("A raiz do seu número é %.2f "%raiz)
         
elif opcao > 1 or opcao < 2:
    print("Por favor. Digite os números que apareçem no menu de opções")