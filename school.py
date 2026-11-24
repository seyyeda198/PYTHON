try:
    with open("names.txt", "r") as file:
        data = file.read()
        print("Existing student names:")
        print(data)

except FileNotFoundError:
    print("File does not exist. Creating new file.")

count = int(input("How many students do you want to add? "))

with open("names.txt", "a") as file:
    for i in range(count):
        name = input("Enter student name: ")
        file.write(name + "\n")

with open("names.txt", "r") as file:
    data = file.read()
    print("\nUpdated student list:")
    print(data)