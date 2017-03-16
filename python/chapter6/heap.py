#coding=utf8
class Heap(object):
    def __init__(self,size):
        self.__size = size

    def max_heapify(self,A,i):
        l = 2 * i
        r = 2 * i + 1
        if l <= self.__size and A[l - 1] > A[i - 1]:
            largest = l
        else:
            largest = i
        if r <= self.__size and A[r - 1] > A[largest - 1]:
            largest = r
        if largest != i:
            A[i - 1],A[largest - 1] = A[largest - 1],A[i - 1]
            self.max_heapify(A,largest)

    def min_heapify(self,A,i):
        l = 2 * i
        r = 2 * i + 1
        if l <= self.__size and A[l - 1] < A[i - 1]:
            minimal = l
        else:
            minimal = i
        if r <= self.__size and A[r - 1] < A[minimal - 1]:
            minimal = r
        if minimal != i:
            A[i - 1],A[minimal - 1] = A[minimal - 1],A[i - 1]
            self.min_heapify(A,minimal)

    def build_max_heap(self,A):
        for i in range((self.__size // 2),0,-1):
            self.max_heapify(A,i)

    def build_min_heap(self,A):
        for i in range((self.__size // 2),0,-1):
            self.min_heapify(A,i)

    def heapUpSort(self,A):               #升序
        self.build_max_heap(A)
        tempsize = self.__size
        for i in range(len(A),0,-1):
            A[0],A[i - 1] = A[i - 1],A[0]
            self.__size -= 1
            self.max_heapify(A,1)
        self.__size = tempsize

    def heapDownSort(self,A):               #降序
        self.build_min_heap(A)
        tempsize = self.__size
        for i in range(len(A),0,-1):
            A[0],A[i - 1] = A[i - 1],A[0]
            self.__size -= 1
            self.min_heapify(A,1)
        self.__size = tempsize
