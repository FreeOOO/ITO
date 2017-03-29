import random
def randomized_partition(A,p,r):
    temp = random.randint(p,r)
    A[r],A[temp] = A[temp],A[r]
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] < x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i + 1],A[r] = A[r],A[i + 1]
    return i + 1

def randomized_quicksort(A,p,r):
    if p < r:
        q = randomized_partition(A,p,r)
        randomized_quicksort(A,p,q - 1)
        randomized_quicksort(A,q + 1,r)

if __name__ == '__main__':
    A = [1,4,6,2,6,84,7,2,62,5,1,23]
    randomized_quicksort(A,0,len(A) - 1)
    print(A)
