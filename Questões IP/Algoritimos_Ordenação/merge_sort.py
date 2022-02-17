#import random
import time

def merge_sort(v, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(v, p, q)
        merge_sort(v, q+1, r)
        intercalar(v, p, q, r)
        
def intercalar(v, p, q, r):
    temp = v.copy()
    
    i = p
    j = q + 1
    k = p
    while k <= r:
        if i > q:
            #primeiro sub-vetor já terminou
            #copiar todos os elementos do segundo sub-vetor
            v[k] = temp[j]
            j += 1
        elif j > r:
            #segundo sub-vetor já terminou
            #copiar todos os elementos do segundo sub-vetor
            v[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            #se o elemento do primeiro sub-vetor for menor (ou igual)
            #copiar esse elemento menor (ou igual)
            v[k] = temp[i]
            i += 1
        else:
            #se o elemento do segundo sub-vetor for maior
            #copar esse elemento
            v[k] = temp[j]
            j += 1
            
        k += 1

#vetor = list(range(0,100000))
#random.shuffle(vetor)
#vetor.reverse()
vetor = [3,0,1,8,7,2,5,4,9,6]

antes = time.time()
merge_sort(vetor, 0, len(vetor)-1)

depois = time.time()
total = (depois - antes) * 1000
print("O tempo total da ordenação foi: %0.2f ms" % total)
print(vetor)

