#sorted array
l=[23,34,44,66,72]
#reverse sorted array
l1=[72,62,42,34,23]
count=0
for i in range(len(l)):
     for j in range(len(l1)):
         if l[i]==l1[j]:
             count+=1
print(count)