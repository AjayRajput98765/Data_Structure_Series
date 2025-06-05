# Creating an array

arr = [10,20,30,40]
print("Array : ",arr)

#Accessing array elements

print(arr[1])

#adding an element in array

arr.append(50)
print(arr)

#Insert an element at index 2

arr.insert(2,60)
print(arr)

#deleting an element

arr.remove(60)
print(arr)

#traversing every element

for i in arr:
    print(i)