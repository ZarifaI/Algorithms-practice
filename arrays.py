# Accessing arrays

new_list = [1, 2, 3] # the values arent stored in memory,  instead the values 1 2 3 are stored elsewhere in memory and the array stores references to each of those objects to access a value we use a subscript along with an index value. 
result = new_list[2]
print(result) 

# Searching for a value in an array .

# we are using linear search. For shorter arrays even if list is not sorted, using linear search may be still fast enough
# we could also sort and then use binary search

if 1 in new_list: print(True) # this is one of the ways to search . using "in" operator . This runs a linear search operation

for n in new_list: # or using for loop and perform comparison operation 
    if n == 1:
        print(True)
        
        break

# Inserting  
# There are three types of insert operations 
# True insert - using index value where we can insert an element anywhere in the list - this operation has Linear Runtime
# second way is appending - it ismple adds the item to the end of the list. Costant time operation , but depends on language 

numbers = []
numbers.append(2)
print(numbers)

numbers = []
numbers.extend([4,5,6])
print(numbers)  

# Deleting operations 
# O(n) Linear Runtime



