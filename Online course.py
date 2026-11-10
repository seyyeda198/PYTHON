Frontend = {"Zarah", "Kevin", "Alex", "Sana"}
Backend = {"Sophia", "Emily", "Zarah", "Ryan"}

Backend.add("Emma")
print(Backend)

Frontend.remove("Kevin")
print(Frontend)

print(Frontend & Backend)
print(Backend - Frontend)

student_list =len(Frontend | Backend)
print(student_list)

courses = {
   "Frontend": len(Frontend),
    "Backend": len(Backend)
}

for x, y in courses.items():
    print(x, y)

new_courses = {course: count for course, count in courses.items()}
new_courses["Fullstack"] = sum(courses.values())

print(new_courses)
