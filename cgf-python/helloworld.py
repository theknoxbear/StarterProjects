print("Hello, World!")

if 5 > 2:
    print("Five is greater than two!")

# This is a comment

x = 5  # 5 is an integer
y = "Jade"  # Jade is a string
print(x)
print(y)

x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

# variables are case-sensitive and A and a are different
# variables must start with a letter or an underscore and cannot start with a number.
# A variable name can only contain alphanumeric characters and underscores

# You can assign values to multiple variables on one line
a, b, c = "Red", "Yellow", "Orange"
print(a)
print(b)
print(c)

# You can assign the same value to multiple variables in one line

d = f = g = "Rainbows"
print(d,f, g)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables.
# This is called unpacking.

fruits = ["Cherries", "Strawberries", "Blueberries"]
j, k, L = fruits
print(j)
print(k)
print(L)


