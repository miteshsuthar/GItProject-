# ar=[6,4,5,3,1,8,7,9]
# k=9
# sum=0
# sum2 = k*(k+1)//2
# for i in ar:
#     sum=sum+i
# print(sum2-sum)
#only approach is apply in sorted array 
ar1=[1,2,3,5,6,7,8,9]
k=9
n=len(ar1)
for i in range(0,n):
    if ar1[i]-i !=1:
       print(i+1)
       break