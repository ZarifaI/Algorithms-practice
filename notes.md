# Big O Notation , Time Complexirt  Cheat sheet
# Source - https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/

how you know which algorithm has which time complexity.

When your calculation is not dependent on the input size, it is a constant time complexity (O(1)).
When the input size is reduced by half, maybe when iterating, handling recursion, or whatsoever, it is a logarithmic time complexity (O(log n)).
When you have a single loop within your algorithm, it is linear time complexity (O(n)).
When you have nested loops within your algorithm, meaning a loop in a loop, it is quadratic time complexity (O(n^2)).
When the growth rate doubles with each addition to the input, it is exponential time complexity (O2^n).

# Examples 

# Constant Time: O(1)

def first_element(array):
    return array[0]

score = [12, 55, 67, 94, 22]
print(first_element(score))  # Output: 12

# The function above will require only one execution step, meaning the function is in constant time with time complexity O(1)


# Linear Time: O(n)

def calc_factorial(n):
    factorial = 1
    for i in range(2, n + 1): # Starting from 2 avoids this redundant operation and is thus more efficient.
        factorial *= i
    return factorial

print(calc_factorial(5))  # Output: 120

# The fact that the runtime depends on the input size means that the time complexity is linear with the order O(n).


# Logarithm Time: O(log n)   Second Best 

# This is similar to linear time complexity, except that the runtime does not depend on the input size but rather on half the input size. When the input size decreases on each iteration or step, an algorithm is said to have logarithmic time complexity.
# This method is the second best because your program runs for half the input size rather than the full size. After all, the input size decreases with each iteration. A great example is binary search functions

def binary_search(array, target):
    first_index = 0
    last_index = len(array) - 1

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2

        if array[middle_index] == target:
            return middle_index

        if array[middle_index] > target:
            last_index = middle_index - 1
        else:
            first_index = middle_index + 1

    return -1

score = [12, 22, 45, 67, 96]
print(binary_search(score, 96))  # Output: 4

# Because for every iteration the input size reduces by half, the time complexity is logarithmic with the order O(n log n).


# Quadratic Time: O(n^2)

# When you perform nested iteration, meaning having a loop in a loop, the time complexity is quadratic, which is horrible.

def match_elements(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return f"Match found at {i} and {j}"
    return "No matches found 😞"

fruit = ["🍓", "🍐", "🍊", "🍌", "🍍", "🍑", "🍎", "🍈", "🍊", "🍇"]
print(match_elements(fruit))  # Output: "Match found at 2 and 8"

# In the example above, there is a nested loop, meaning that the time complexity is quadratic with the order O(n^2).

# Exponential Time: O(2^n) 

# You get exponential time complexity when the growth rate doubles with each addition to the input (n), often iterating through all subsets of the input elements.

def recursive_fibonacci(n):
    if n < 2:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

print(recursive_fibonacci(6))  # Output: 8
