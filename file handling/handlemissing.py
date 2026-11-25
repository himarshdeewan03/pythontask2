try:
    data = open("data.txt").read()
    print(data if data else "File is empty")
except:
    print("File not found")
