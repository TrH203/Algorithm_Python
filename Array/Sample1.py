# This is array
arr = [1,2,3,4,5]

# Create a Array
arr1 = [] # Create a Array
n = int(input("Enter len of arr: "))
for i in range(n):
    arr1.append(int(input(f"Enter the {i+1} element: ")))

print(*arr1,sep=' ')

# Other way
arr2 = []
n = int(input("Enter len of arr: "))
[arr2.append(int(input(f"Enter the {i+1} element: "))) for i in range(n)]

print(*arr2,sep=" ")
