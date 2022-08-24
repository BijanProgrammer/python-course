file = open("08_file_example.txt", "r")
lines = file.readlines()
lines.insert(5, "This is Changed\n")
file.close()

file = open("08_file_example.txt", "w")
file.write("".join(lines))
file.close()
