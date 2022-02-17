import random
import time

def insertionsort(v):
    
    i = 1
    while i < len(v):
        
        troca = False
        temp = v[i]
        
        j = i - 1
        while j >= 0 and v[j] > temp:
            v[j+1] = v[j]
            troca = True
            j -= 1
        
        if troca:
            v[j+1] = temp
        
        i += 1 
    
    
    return v

vetor = list(range(0, 10000))

random.shuffle(vetor)

antes = time.time()
vetor_ordenado = insertionsort(vetor.copy())
depois = time.time()
total = depois - antes
print("Tempo total: %f ms" % (total*1000))
#print(vetor_ordenado)
