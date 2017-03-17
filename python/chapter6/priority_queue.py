from heap import *

class PriorityQueue(object):
    def __init__(self,size,heap):
        self.size = size
        self.heap = heap

    def heap_maximum(self,A):
        return A[1 - 1]

    def heap_extract(self,A):
        if self.size < 1:
            print('error,heap underflow!!')
            return None
        maxnum = A[1 - 1]
        A[1 - 1],A[self.size - 1] = A[self.size - 1],A[1 - 1]
        self.size -= 1
        self.heap.setsize(self.size)
        self.heap.max_heapify(A,1)
        return maxnum

    def heap_increase_key(self,i,key):
        if A[i - 1] > key:
            print('error')
            return 0
        A[i - 1] = key
        while i // 2 > 0 and A[i - 1] > A[i // 2 - 1]:
            A[i - 1],A[i // 2 - 1] = A[i // 2 - 1],A[i - 1]
            i = i // 2

    def max_heap_insert(self,A,key):
        self.size += 1
        self.heap.setsize(self.size)
        A[self.size - 1]= float('-Inf')
        self.heap_increase_key(self.size,key)

    def printqueue(self,A):
        print(A[0:self.size - 1])

if __name__ == '__main__':
    A = [4,1,3,2,16,9,10,14,8,7]
    heap = Heap(len(A))
    heap.build_max_heap(A)
    priorityQueue = PriorityQueue(len(A),heap)
    print(priorityQueue.heap_maximum(A))
    priorityQueue.printqueue(A)
    print(priorityQueue.heap_extract(A))
    priorityQueue.printqueue(A)
    print(priorityQueue.max_heap_insert(A,20))
    priorityQueue.printqueue(A)
