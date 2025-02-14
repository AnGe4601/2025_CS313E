'''
class OurCircle:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color

    def calc_area(self):
        area = self.radius ** 2 * 3.14
        return area 

def main():
    first_circle = OurCircle(20, 50, 50, 'blue')
    first_circle_area = calc()
    print(first_circle_area)
    first_circle_area.color #gettiing the attribute
'''   

def __str__(self):
    return str(self.radius) + " " + str(self.color)
