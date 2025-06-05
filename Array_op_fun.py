def insert_element(arr,index,value):
    arr.insert(index,value)
    return arr

def delete_element(arr,value):
    arr.remove(value)
    return arr

def linear_search(arr,ele):
    if ele in arr:
        print("Found at index :",arr.index(ele))
    else:
        print("Element not found !")
        
arr = [7,8,9,4,5,6,1,2,3]
x = insert_element(arr,4,15)
print(x)
y = delete_element(arr,1)
print(y)
linear_search(arr,2)
