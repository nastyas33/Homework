#1

num = input("Please enter your numbers: ")
list_new = []

for i in num.split(','):
    list_new.append(int(i))

print(list_new)
print(tuple(list_new))

#2 решение
string_numbers = input("Enter numbers: ")

list_numbers = string_numbers.split(' , ')
tuple_numbers = tuple(list_numbers)

print(list_numbers, type(list_numbers))
print(tuple_numbers, type(tuple_numbers))