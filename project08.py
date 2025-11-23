'''Output dictionary which contains only the odd numbers that are 
present in the input list as keys and their cubes as values using List Comprehension'''

# Step 1: Take a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Step 2: Use dictionary comprehension
odd_cubes = {n: n**3 for n in numbers if n % 2 != 0}

# Step 3: Print result
print("Input list:", numbers)
print("Output dictionary:", odd_cubes)