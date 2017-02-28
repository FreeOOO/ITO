def find_max_crossing_subarray(A,begin,mid,end):
    leftsum = float('-inf')
    sum = 0
    for x in range(mid,-1,-1):
        sum += A[x]
        if sum > leftsum:
            leftsum = sum
            maxleft = x
    rightsum = float('-inf')
    sum = 0
    for x in range(mid + 1,end + 1):
        sum += A[x]
        if sum > rightsum:
            rightsum = sum
            maxright = x
    return (maxleft,maxright,leftsum + rightsum)

def find_maximum_subarray(A,begin,end):
    if begin == end:
        return (begin,end,A[begin])
    else:
        mid = (begin + end) // 2
        leftlow,lefthigh,leftsum = find_maximum_subarray(A,begin,mid)
        rightlow,righthigh,rightsum = find_maximum_subarray(A,mid + 1,end)
        crosslow,crosshigh,crosssum = find_max_crossing_subarray(A,begin,mid,end)
        if leftsum >= rightsum and leftsum >= crosssum:
            return (leftlow,lefthigh,leftsum)
        elif rightsum >= leftsum and rightsum >= crosssum:
            return (rightlow,righthigh,rightsum)
        else:
            return (crosslow,crosshigh,crosssum)

if __name__ == '__main__':
    A = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    low,high,sum = find_maximum_subarray(A,0,len(A) - 1)
    print(low,high,sum)
