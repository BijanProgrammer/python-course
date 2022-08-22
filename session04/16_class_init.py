class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


p1 = Point()
print(f"({p1.x}, {p1.y})")

p2 = Point(23, 42)
print(f"({p2.x}, {p2.y})")
