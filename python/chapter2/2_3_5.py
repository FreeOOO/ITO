def search(A,begin,end,temp):
    if begin <= end:
        index = (begin + end) // 2
        if A[index] == temp:
            return index
        elif A[index] < temp:
            return search(A,index + 1,end,temp)
        elif A[index] > temp:
            return search(A,begin, index - 1,temp)
    return -1

if __name__ == '__main__':
    A = [1,4,6,8,23,25,29,35,37,46,78]
    print(search(A,0,len(A) - 1,7))
