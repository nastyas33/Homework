#1 решение

x = input("Please enter the value of the variable 'x': ")
y = input("Please enter the value of the variable 'y': ")
z = x
x = y
y = z
print(x, y)

#2 решение
a = input("Please enter the value of the variable 'a': ")
b = input("Please enter the value of the variable 'b': ")
a, b = b, a
print(a,b)