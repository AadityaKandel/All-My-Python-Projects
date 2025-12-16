
'''
# Create a list and a tuple with 5 elements and print them.
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
print(list1)
print(tuple1)
'''

'''
# Find the length of a list and a tuple.
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
len_of_list1 = len(list1)
len_of_tuple1 = len(tuple1)
print(f"Length of List: {len_of_list1}\nLength of Tuple: {len_of_tuple1}")
'''

'''
# Access the 3rd element from a list and a tuple.
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
print(f"Third element of List: {list1[2]}\nThird element of Tuple: {tuple1[2]} ")
'''

'''
# Check whether an element exists in a list and a tuple.
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
if 1 in list1 and 2 in tuple1:
    print("True") # Indicates that both elements exist
'''

'''
# Print all elements of a list and a tuple using a loop.
list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)

print("Items of List1")
for elements_of_list in list1:
    print(f"{elements_of_list}\n",end="")
print("\nItems of Tuple1")
for elements_of_tuple in tuple1:
    print(f"{elements_of_tuple}\n",end="")
'''
    

'''
# Find the maximum and minimum values in a list and a tuple.
list1 = [1,2,3,4,5]
tuple1 = (6,7,8,9,10)
print("Maximum value of list1:",max(list1))
print("Maximum value of tuple1",max(tuple1))
'''

'''
# Convert a list into a tuple.
list1 = [1,2,3,4,5]
converted_into_tuple = tuple(list1)
print(converted_into_tuple)
'''

'''
# Convert a tuple into a list.
tuple1 = (1,2,3,4,5)
converted_into_list = list(tuple1)
print(converted_into_list)
'''

'''
# Add an element to a list and display the result.
list1 = [1,2,3,4,5]
list1.append(6) # Appends as the last item in a list
print(list1)
list1.insert(0,'Ram') # Inserts to the given index in a list
print(list1)
'''

'''
# Remove an element from a list.
list1 = [1,2,3,4,5]
print("Initial: ",list1)

# Method 1: pop()
list1.pop(0) # Removes the item in the given index
print("Pop: ",list1)

# Method 2: remove()
list1.remove(2) # Removes the given item directly
print("Remove: ",list1)

# Method 3: del
del list1[1] # Deletes the item in the given index
print("Del: ",list1)
'''

'''
# Replace an element in a list.
list1 = [1,2,3,4,5]
list1[0]=10
print(list1)
'''

'''
# Count how many times an element appears in a list and a tuple.
list1 = [1,2,3,2,4,5]
tuple1 = (1,2,3,4,3,5,3,6,3)
count=0
for x in list1:
    if x==2:
        count+=1
print(f"The item {list1[1]} appears {count} times in a list")
count=0
for x in tuple1:
    if x==3:
        count+=1
print(f"The item {tuple1[2]} appears {count} times in a tuple")
'''

'''
# Reverse a list and a tuple.
list1=[1,2,3,4,5]
tuple1=(5,4,3,2,1)
list1.reverse()
print(list1)
temp = list(tuple1)
temp.reverse()
tuple1 = tuple(temp)
print(tuple1)
'''

'''
# Sort a list and a tuple.
list1=[5,4,3,2,1]
tuple1=(9,8,7,6,5)
temp = list(tuple1)
temp.sort()
list1.sort()
tuple1 = tuple(temp)
print(list1)
print(tuple1)
'''

'''
# Find the sum of all numeric elements in a list and a tuple.
list1 = [1,2,3,4,5]
tuple1 = (6,7,8,9,10)
print("Sum of list1: ",sum(list1))
print("Sum of tuple1: ",sum(tuple1))
'''

'''
# Print only even numbers from a list and a tuple.
list1=[1,2,3,4,5]
tuple1=(6,7,8,9,10)

print("Even numbers of a list: ")
for items in list1:
    if items%2==0:
        print(items)
print("Even numbers of a tuple: ")
for items in tuple1:
    if items%2==0:
        print(items)
'''

'''
# Remove duplicate elements from a list.
list1 = [1,1,1,2,2,3,4,2,5,5]
print(list(set(list1)))
'''

'''
# Replace the last element of a tuple.
tuple1 = (1,2,3,4,5)
temp = list(tuple1)
temp[-1]="HAHA REPLACED!!"
tuple1 = list(temp)
print(tuple1)
'''

'''
# Create a nested list and print all elements.
list1 = [[1,2,3,4,5],[6,7,8,9,10]]
for index in range(len(list1)):
    print(f"\nItems of {index} index in list1")
    for items in list1[index]:
        print(items)
'''

'''
# Create a nested tuple and access inner elements.
tuple1 = ((1,2,3,4,5),("one","two","three","four","five"))
for index in range(len(tuple1)):
    print(f"\nItems of {index} index in tuple1")
    for items in tuple1[index]:
        print(items)
'''

'''
# Find the second largest element in a list and a tuple.
list1 = [1,2,3,4,5]
tuple1 = (6,7,8,9,10)

list1.remove(max(list1))
temp = list(tuple1)
temp.remove(max(tuple1))
print(max(list1))
print(max(temp))
'''

'''
# Check if a list is empty.
list1 = []
if len(list1)==0:
    print("Yes! The list is empty")
else:
    print("No! The list isn't empty")
'''

'''
# Check if a tuple is empty.
tuple1 = tuple()
if len(tuple1)==0:
    print("Yes! The tuple is empty")
else:
    print("No! The tuple isn't empty")
'''   

'''
# Merge two lists and two tuples.
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list1.extend(list2)
tuple1 = (11,12,13,14,15)
tuple2 = (16,17,18,19,20)
tuple1 = tuple1+tuple2
print(list1)
print(tuple1)
'''

'''
# Create a list and tuple of squares from 1 to n.
list1 = []
tuple1 = tuple()
n = 7 # Say 20
for x in range(n):
    list1.append(x**2)
    tuple1+=(x**2,)
print(list1)
print(tuple1)
'''

