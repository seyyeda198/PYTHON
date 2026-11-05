python = """    Python is an interpreted, high-level and general-purpose programming language.
It is an object-oriented language too, which simply means it can model entities in the real world.
This Python course is easy to learn and useful for many applications."""

print("Length:", len(python))

print("First character:", python[0])
print("Last character:", python[-1])
print("Preview:", python[:50])

replace = python.replace("Python", "PYTHON")
print(replace)

tolower = python.lower()
print(tolower)

whitespace = python.strip()
print(whitespace)

words = python.split()
print("Words:", words)

if "course" in python:
    print("The word course is found.")

print("The course description is {} characters long and has {} words.".format(len(whitespace), len(words)))