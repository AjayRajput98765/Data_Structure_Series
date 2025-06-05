arr = [4,5,6,7,8,9]

#insert an element 
arr.insert(3,10)
print(arr)

#Deletion of an element
arr.remove(8)
print(arr)


#Searching for element 10

if 10 in arr:
    print("Element found at",arr.index(10))
else:
    print("Element not found")
