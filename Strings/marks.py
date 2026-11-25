marks = []

for i in range(5):
    m = int(input("Enter mark: "))
    marks.append(m)

total = sum(marks)
average = total / 5
highest = max(marks)
lowest = min(marks)

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
