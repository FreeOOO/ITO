def insertion_sort(arr):
    for index in range(1,len(arr)):
        temp = arr[index]
        for ind in range(index)[-1::-1]:
            if arr[ind] > temp:
                arr[ind + 1] = arr[ind]
            else:
                arr[ind + 1] = temp
                break

if __name__ == '__main__':
    arr = [1,4,5,2,64,23,61,2,553,2,1]
    insertion_sort(arr)
    print(arr)
