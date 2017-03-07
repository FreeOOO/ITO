def find2(A):
    max1 = float('-inf')
    sum1 = A[0]
    low,high = 0,0
    for i in range(1,len(A)):
        tempmax = float('-inf')
        tempsum = 0
        for j in range(i,low - 1,-1):
            tempsum += A[j]
            if tempsum > tempmax:
                tempmax = tempsum
                tempindex = j
        if tempmax > sum1:
            sum1 = tempmax
            low = tempindex
            high = i
    return low,high,sum1

if __name__ == '__main__':
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    low,high,sum1 = find2(A)                                     #线性查找
    print(low,high,sum1)
