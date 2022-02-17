import random
import time

def quicksort(v, p, r):
    if p < r:
        q = particionar(v, p, r)
        quicksort(v, p, q-1) #pivotar a esquerda
        quicksort(v, q+1, r) #pivotar a direita
        
def particionar(v, p, r):
    x = v[r] #escolhendo o pivô
    i = p - 1
    j = p
    while j < r:
        if v[j] < x:
            i += 1
            trocar(v, i, j) #puxando o elemento menor que o pivô
        j += 1
    
    trocar(v, i+1, r)
    
    return i+1

def trocar(v, n, m):
    temp = v[n]
    v[n] = v[m]
    v[m] = temp

vetor = list(range(0,10))
random.shuffle(vetor)
#vetor.reverse()
#vetor = [3,0,1,8,7,2,5,4,9,6]

antes = time.time()
quicksort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois - antes) * 1000
print("O tempo total da ordenação foi: %0.2f ms" % total)
print(vetor)

