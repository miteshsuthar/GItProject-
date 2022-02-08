N=int(input())
div=0
st=str(N)
for i in st:
    div=div+int(i)
x=N//div
print(x)
if x==N:
    print('Yes')
else:
    print('No')

