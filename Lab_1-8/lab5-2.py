class circle:
    def __init__(self, radius):
        self.radius = radius
        pass
    def get_radius(self):
        return "The circle radius is: {}".format(self.radius)
    def set_radius(self, new_radius):
        new_radius=int(input("Enter new radius:"))
        return "The new circle radius is: {}".format(new_radius)
circleA = circle(10)
print(circleA.get_radius())
print(circleA.set_radius())
