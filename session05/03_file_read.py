file = open("03_file_read.txt", "r")

# returns everything
# print(file.read())

# returns first 20 characters
# print(file.read(20))
# returns next 5 characters
# print(file.read(5))

# returns first line
# print(file.readline())
# returns second line
# print(file.readline())

# loops content
for x in file:
    print(x)
