FILE = "students.txt"


def load():
    students = []
    try:
        f = open(FILE, "r")
        for line in f:
            name, roll, marks = line.strip().split(",")
            students.append([name, roll, float(marks)])
        f.close()
    except FileNotFoundError:
        pass
    return students


def save(students):
    f = open(FILE, "w")
    for s in students:
        f.write(f"{s[0]},{s[1]},{s[2]}\n")
    f.close()


def add(students):
    if len(students) == 3:
        print("Only 3 students allowed!")
        return

    name = input("Name: ")
    roll = input("Roll number: ")
    try:
        marks = float(input("Marks: "))
    except ValueError:
        print("Enter valid numbers!")
        return

    students.append([name, roll, marks])
    save(students)
    print("Student saved!")


def view(students):
    for s in students:
        print("Roll:", s[1], "| Name:", s[0], "| Marks:", s[2])


def search(students):
    roll = input("Enter roll number: ")
    for s in students:
        if s[1] == roll:
            print("Found:", s[0], "| Marks:", s[2])
            return
    print("Not found!")


def average(students):
    if len(students) == 0:
        print("No students!")
        return
    total = 0
    for s in students:
        total += s[2]
    print("Average marks:", total / len(students))


students = load()

while True:
    print("\n1. Add student")
    print("2. View all students")
    print("3. Search student by roll number")
    print("4. Calculate average marks")
    print("5. Exit")

    ch = input("Choice: ")

    if ch == "1":
        add(students)
    elif ch == "2":
        view(students)
    elif ch == "3":
        search(students)
    elif ch == "4":
        average(students)
    elif ch == "5":
        break
    else:
        print("Invalid choice!")
