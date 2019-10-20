def missingNumber(arr):
    n = len(arr)
    gap = (arr[n-1]-arr[0])//n
    if gap==0:
        return 0
    for i in range(n-1):
        diff = arr[i+1]-arr[i]
        if diff!=gap:
            return arr[i]+gap

if __name__=='__main__':
    result = missingNumber([15,13,12])
