from heap import *

if __name__ == '__main__':
    A = [4,1,3,2,16,9,10,14,8,7]
    heap1 = Heap(len(A))
    heap1.heapUpSort(A)
    print(A)
    heap1.heapDownSort(A)
    print(A)
