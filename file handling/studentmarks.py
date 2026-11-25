name = input("Name: ")
marks = input("Marks: ")

open("student.txt", "w").write(name + " - " + marks)
print(open("student.txt").read())
