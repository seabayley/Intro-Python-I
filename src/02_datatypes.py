"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"


def add_str_to_int(string, integer):
    try:
        return (int(string) + integer)
    except ValueError:
        print("That value cannot be coerced into an Integer.")


def add_int_to_str(integer, string):
    try:
        return (str(integer) + string)
    except TypeError:
        print("That value cannot be coerced into a String.")

# Write a print statement that combines x + y into the integer value 12


print(add_str_to_int(y, x))

# Write a print statement that combines x + y into the string value 57

print(add_int_to_str(x, y))
