python = {"Zarah", "Kevin", "Alex", "Sana"}
Data_science = {"Sophia", "Emily", "Zarah", "Ryan"}

python.add("Emma")
print(python)

Data_science.remove("Emily")
print(Data_science)

print(python & Data_science)
print(python - Data_science)
print(python | Data_science)

course = {
    "python" : 5,
    "Data_science" : 3
}
print(course)

for x, y in course.items():
    print("Course:", x, ", Students:", y)

new_course = {
    "Python": 10,
    "Java": 20,
    "SQL": 15
}
changed = {x: y*2 for x, y in new_course.items()}
print(changed)
