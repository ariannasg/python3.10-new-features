# new pattern matching using match and case, including a default case
from typing import List


def http_error(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 500:
            return "Server error"
        case _:
            return "Unknown"


# combining literals on the same case
def http_error2(status):
    match status:
        case 200:
            return "OK"
        case 400 | 404 | 500:
            return "Error"
        case _:
            return "Unknown"


# advanced use with classes
class Point:
    __match_args__ = ["x", "y"]

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def location(point):
    match point:
        case Point(x=x_val, y=0):
            print(f"X={x_val} and the point is on the X axis")
        case Point():
            print(f"The point is elsewhere")
        case _:
            print(f"Not a point")


location("a")
location(Point(x=5, y=0))
location(Point(x=5, y=5))



# nested patterns
class PointList:
    z: List[Point]

    def __init__(self, z):
        self.z = z

def match_points(points):
    match points:
        case []:
            print(f"No points in the list")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Point 1 has Y={y1} and Point 2 has Y={y2}")
        case _:
            print(f"Not what's expected")


match_points([])
match_points(PointList([Point(0, 5), Point(0, 8)]))
match_points(PointList([Point(0, 5)]))
match_points(Point(0, 5))
match_points("a")
