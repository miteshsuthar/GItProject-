# 6 4
# 1 12 -5 -6 50 3
arr=[1,12,-5,-6,50,3]
n=6
k=4
sum=0
for i in range(k):
    sum =sum+arr[i]
max_sum=sum
second_sum=-999999999
for i in range(k,n):
    sum= max_sum
    sum=sum-arr[i-k]+arr[i]
    second_sum=sum
    if max_sum>second_sum:
        second_sum=sum
    
    else:
        max_sum=sum
print(second_sum//4)