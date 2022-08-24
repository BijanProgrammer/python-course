file = open("03_file_read.txt", "r")

# for i in range(9):
#     file.readline()
#
# line10 = file.readline()
#
# print(line10)


lines = file.readlines()
print(lines[9])
