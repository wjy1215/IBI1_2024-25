# Write a program that prints the first 10 numbers of the sequence 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.
a=[0]*10
a[0]=1
print(a[0],end=" ")
for i in range(1, 10):
    a[i]=i+a[i-1]+1
    print(a[i],end=" ")


