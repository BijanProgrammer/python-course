# Good Morning (05:00 => 11:59)
# Good Day (12:00 => 14:59)
# Good Afternoon (15:00 => 16:59)
# Good Evening (17:00 => 19:59)
# Good Night (20:00 => 04:59)

time = input("time: ")
hour = int(time[:2])

if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 15:
    print("Good Day")
elif 15 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 20:
    print("Good Evening")
elif 20 <= hour < 24 or 0 <= hour < 5:
    print("Good Night")
else:
    print("Please enter a time in HH:mm format")
