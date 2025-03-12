# Write a program that prints the first 10 numbers of the sequence 1, 3, 6, 10, 15, 21, 28, 36, 45, 55.
a=[0]*10 #initialize the list with 10 zeros
a[0]=1   #set the first element to 1
print(a[0],end=" ") #print the first element
#loop through the list from the second element to the 10th element
for i in range(1, 10): #    1, 2, 3, 4, 5, 6, 7, 8, 9
    #calculate the next element in the sequence
    #the next element is the current element plus the previous element plus 1
    a[i]=i+a[i-1]+1   
    print(a[i],end=" ") #print the next element
# Output: 1 3 6 10 15 21 28 36 45 55


