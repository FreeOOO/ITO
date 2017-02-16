def merge(arr,p,q,r):       #merge arr[p,q] and arr[q + 1,r]
    i = p
    j = q + 1
    temp = []
    while i <= q and j <= r:
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i = i + 1
        else:
            temp.append(arr[j])
            j = j + 1
    if i <= q:
        while i <= q:
            temp.append(arr[i])
            i = i + 1
    elif j <= r:
        while j <= r:
            temp.append(arr[j])
            j = j + 1
    for index in range(p,r + 1):
        arr[index] = temp[index - p]

def merge_sort(arr,begin,end):
    if begin < end:
        merge_sort(arr,begin,(begin + end) // 2)
        merge_sort(arr,(begin + end) // 2 + 1,end)
        merge(arr,begin,(begin + end) // 2,end)

if __name__ == '__main__':
    arr = [1,2,5,3,64,234,63,2234,645,243,623,21,3,6,3,6,34,43]
    merge_sort(arr,0,len(arr) - 1)
    print(arr)
