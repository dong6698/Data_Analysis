file = open("testfile.txt", "r+")

print(file.name)
print(file.readline())
print(file.readline())


file.close()