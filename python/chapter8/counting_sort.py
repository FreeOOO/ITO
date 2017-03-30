def counting_sort(A,B,k):
    C = [0] * (k + 1)
    for i in A:
        C[i] += 1
    for i in range(1,k + 1):
        C[i] += C[i - 1]
    D = A[:]
    D.reverse()
    for i in D:
        B[C[i] - 1] = i
        C[i] -= 1

if __name__ == '__main__':
    A = [2,5,3,0,2,3,0,3]
    B = [0 for i in range(len(A))]
    #maxnum = float('-Inf')
    #for i in A:
    #    maxnum = i if maxnum < i else maxnum
    maxnum = max(A)
    counting_sort(A,B,maxnum);
    print(B)

