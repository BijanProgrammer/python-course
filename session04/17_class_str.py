class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = Point()
print(p1)

p2 = Point(23, 42)
print(p2)
