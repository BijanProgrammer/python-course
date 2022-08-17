people = ["Bijan", "Reza", "Ali", "Mahdi", "Mohammad", "Alireza", "Babak"]

# first = people[0]
# second = people[1]
# third = people[2]

[first, second, third, *etc] = people
print(first)
print(second)
print(third)
print(etc)
