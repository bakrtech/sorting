def bubbleSort(L):
    n=len(L)
    for i in range(n):
        for j in range(0,n-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
UL=eval(input("Enter the unsorted : \n"))
bubbleSort(UL)
print("The sorted list is ",UL)
