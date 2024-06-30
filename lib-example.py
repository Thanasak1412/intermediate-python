import os

folder = os.getcwd()

print(folder)

with os.scandir(folder) as folder:
    for entry in folder:
        print(f' - {entry}')