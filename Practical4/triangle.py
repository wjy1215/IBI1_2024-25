a=[0]*10
a[0]=1
print(a[0],end=" ")
for i in range(1, 10):
    a[i]=i+a[i-1]+1
    print(a[i],end=" ")
# What does this code do?

