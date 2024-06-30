# Iterating over two lists in parallel:
names = ["Alice", "Bob", "Charlie"]
scores = [10, 20, 30]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")
    
# Creating a dictionary from two lists:
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

dictionary = dict(zip(keys, values))

print(dictionary)

# Combining multiple iterables:
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [True, False, True]

zipped = zip(list1, list2, list3)

for item in zipped:
    print(item)
    
"""Different lengths
    if the input iterables are difference lengths, `zip` will stop creating tuples
    when the shortest input iterable are exhausted.
"""
list1 = [1, 2, 3]
list2 = ["a", "b", "c", "d"]

for item in zip(list1, list2):
    print(item)
    
"""unzipping
    You can unzip a list of tuples using the `zip` function with the `*` operator
"""
zipped = [(1, "a"), (2, "b"), (3, "c")]
list1, list2 = zip(*zipped)

print(list(list1))
print(list(list2))