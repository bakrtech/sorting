lst=eval(input("Enter the list to be searched : "))
item = int(input("Enter the number to be searched : "))
lst.sort()
k = int((len(lst))/2)
print("THE NEW SORTED LIST IS : " ,lst)
if lst[k]< item:
    for i in range(k,len(lst)):
        if lst[i] == item:
            print("The element ",item ," is at index number:",i," OR at ",i+1," place" )
            break
else:
    for i in range(0,k):
        if lst[i] == item:
            print("The element " ,item , " is at index number: " , i," Or at " , i+1," place")
            break 

