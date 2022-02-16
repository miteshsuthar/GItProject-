def checkkey(arr,n,key,segment):
    for i in range(0,n,segment):
        for j in range(0,segment):
            if i+j<n and arr[i+j]==key:
                j=segment
                break
        if j==segment-1:
            return False
    return True
arr=[3,5,2,4,9,3,1,7,3,11,12,3]
arr=[23,2,321,323,2,23,123,213]
key=3
segment=4
n=len(arr)
result=checkkey(arr,n,key,segment)
print(result)