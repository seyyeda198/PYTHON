fruits = ["apple", "orange", "mango", "grapes"]
vegetables = ["tomato", "potato", "carrot","brinjal"]
beverages = ["Coca-Cola", "Pepsi", "Sprite", "Mirinda"]

fruits.append("pineapple")
print(fruits)

vegetables.insert(1, "cucumber")
print(vegetables)

beverages.pop()
print(beverages)

inventory = [fruits, vegetables, beverages]
print(inventory)

print(fruits[:2])
print(vegetables[-1])

fruits_length = [len(x) for x in fruits ]
print(fruits_length)

print("Water" in beverages)

first_items = (fruits[0], vegetables[0], beverages[0])
print("First Items:", first_items)