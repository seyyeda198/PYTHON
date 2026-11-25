import random
import math

names = input("Enter guest names:")

name_list = names.split(",")

new_list = list(set(name_list))

random_name = random.choice(new_list)

reversed_name = random_name[::-1]

total_names = len(new_list)

sqrt = round(math.sqrt(total_names))

print("Names:", new_list)
print("selected name:", random_name)
print("reversed:", reversed_name)
print("count of names:", total_names)
print("square root:", sqrt)


