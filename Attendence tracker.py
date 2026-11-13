attendance = [18, 20, 19, 15, 21]

full_days = 0

for x in attendance:
    if x >= 20:
        print("class was full")
        full_days = full_days + 1
    else:
        print("class was not full")

print("Full days:", full_days)
print("Total Attendance:", sum(attendance))