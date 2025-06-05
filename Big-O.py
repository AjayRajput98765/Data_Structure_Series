# O(1) 
def get_first_element(arr):
    return arr[0]


# O(n)
def print_all_elements(arr):
    for num in arr:
        print(num)
        
        
# O(n^2)
def print_all_pairs(arr):
    for i in arr:
        for j in arr:
            print(i,j)
            
            
            
arr = [1,2,3]
x = get_first_element(arr)
print(x)