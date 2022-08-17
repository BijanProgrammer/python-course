# by reference
mentors = ["Bijan", "Reza", "Ali"]

seniors = mentors.copy()
seniors.append("Mahdi")
seniors.append("Mohammad")

print(seniors)
print(mentors)

# by value
a = 23
b = a
b += 2
print(a)
print(b)
