# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
for i in range(len(x)):
    if x[i] == 9 and x[i+1] == 10:
        x.insert(i+1, 99)
        break
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000

# with a for loop
stout = []
for i in range(len(x)):
    stout.append(x[i]*1000)
print(stout)

print(list(map(lambda x: x * 1000, x)))  # with map
print([i*1000 for i in x])  # with comprehension
