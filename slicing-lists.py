import random

str = "Hello, World!"

print(str[7:])

names = ["Nina", 'John', "Tim", "Dom", "Test", "Joey"]

print(names[0:-1:2])

new_names = names.copy()

new_names.append("Philip")

print(new_names)
print(names)

numbers = {num: num * num for num in range(11)}

print(numbers)

list_numbers = [num for num in range(0, 101) if num % 2 == 0]

random_even_numbers  = {k: random.choice(range(0, 101, 2)) for k in list_numbers}
 
print(random_even_numbers)