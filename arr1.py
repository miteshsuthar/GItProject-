def ele(ar,n):
     sum=0
     for i in range(n):
        sum=sum+ar[i]
        for j in range(1,n):
            sum =sum+ar[j]
            if sum==0 or ar[i]==0 or ar[j]==0:
                return True
        sum=0
     return False       
ar=[1,5,-3,-2,4]
n=len(ar)
result=ele(ar,n)
print(result)