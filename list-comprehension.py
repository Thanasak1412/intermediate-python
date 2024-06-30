names = ["test1", "test2", "test3"]

upper_names = [name.upper() for name in names]

print(upper_names)

squares = [num * num for num in range(10)]

print(squares)

name_str = ", ".join([f"Name is {name}" for name in names])

print(name_str)

even_squares = [num * num for num in range(6) if num % 2 == 0]

print(even_squares)

str_even = ", ".join([str(even_square) for even_square in even_squares])

print(str_even)

lottery_numbers_str = "2, 123, 103, 102, 100"

max_number = max([int(num) for num in lottery_numbers_str.split(", ")])

print(max_number)