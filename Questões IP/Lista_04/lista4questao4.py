T = [-10, -9, 0, 1, 2, 5, -2, -4]

menor = T[0]
maior = T[0]

soma_T = 0

for temperatura in T:
    soma_T += temperatura
    
    if menor > temperatura:
        menor = temperatura
    
    if maior < temperatura:
        maior = temperatura

média = soma_T / len(T)

print("A média das temperaturas é %f" % média)
print("A menor temperatura é %d" % menor)
print("A maior temperatura é %d" % maior)