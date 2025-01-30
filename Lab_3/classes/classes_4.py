class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y
    
    def move(self):
        self.x += 1
        self.y += 1
        return self.x, self.y
    
    def dist(self, point2):
        return ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5
        
# point1 = Point(3, 4)
# point2 = Point(5, 15)
# print("Coordinates of a point 1 (x, y): ", point1.show())
# print("Coordinates of a point 2 (x, y): ", point2.show())

# print("Coordinates after the point 1 moved (x, y): ", point1.move())
# print("Coordinates after the point 2 moved (x, y): ", point2.move())

# print("Distance between two points: ", point1.dist(point2))