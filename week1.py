# Week 1 - My first Data Science practice
name = "Mahasha Masilo Shaun"
qualification = "Diploma in Mathematical Sciences"
print(f"Name: {name}, Qualification: {qualification}")

marks = [65, 78, 82, 55, 90]
mean = sum(marks) / len(marks)
print(f"Average mark: {mean}")

for mark in marks:
    if mark >= 75:
        print(f"{mark} - Distinction!")