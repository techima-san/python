from math import pi

# runs purely and do not check for invalid radius input
def circle_area(r):
    return pi*(r**2)

radius_list = [2, 0, -3, 2 + 5j, True, "Radius"] # Includes invalid values for a circle radius
message = "Area of circle with r = {radius} is {area}"

for r in radius_list:
    A = circle_area(r)
    print(message.format(radius=r, area=A))
    