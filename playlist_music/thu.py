with open("data.txt", "r" ) as file:
    name = file.readline().strip("\n")
    description = file.readline().strip("\n")
print(name)
print(description)