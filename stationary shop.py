try:
    item = input("Enter the new item name: ")

    with open("items.txt", "a") as file:
        file.write(item + "\n")

    print("\nList of items:")

    with open("items.txt", "r") as file:
        items = file.read()
        print(items)

except FileNotFoundError:
    print("File not found!")