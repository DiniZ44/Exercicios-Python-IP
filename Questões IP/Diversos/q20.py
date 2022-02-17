while True: 
    numero = int(input("Digite um numero inteiro: "))
    
    if numero <= 1:
        print("Digite novamente! Número precisa ser maior que (1).")
        continue
        
    cont_divisoes = 0
    i = numero
    
    while i >=1:
        
        if numero % 1 == 0:
            cont_divisoes = cont_divisoes + 1
        i -=1
            
    if cont_divisoes > 1:
        print("Número não primo")
        
    else:
        print("Número  primo!")
        break