text = input("Enter a word or sentence: ")
counts = {}

for char in text:
    if char in counts:
        counts[char] = counts[char] + 1
    else:
        counts[char] = 1

print(counts)
