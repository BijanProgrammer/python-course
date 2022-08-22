n = int(input("n: "))

# *
# **
# ***
#
# i = 1
# while i <= n:
#     print(i * "*")
#     i += 1

# ***
# **
# *
#
# i = 0
# while i < n:
#     print((n - i) * "*")
#     i += 1

#   *
#  **
# ***
#
# i = 1
# while i <= n:
#     print((n - i) * " " + i * "*")
#     i += 1

# ***
#  **
#   *
#
# i = 0
# while i < n:
#     print(i * " " + (n - i) * "*")
#     i += 1

#   *
#  ***
# *****
#  ***
#   *
#
# i = 1
# while i <= 2 * n - 1:
#     spaces_count = (2 * n - 1 - i) // 2
#     print(spaces_count * " " + i * "*")
#     i += 2
#
# i = 2 * n - 3
# while i >= 1:
#     spaces_count = (2 * n - 1 - i) // 2
#     print(spaces_count * " " + i * "*")
#     i -= 2
