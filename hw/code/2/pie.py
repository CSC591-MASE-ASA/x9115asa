import math
from swampy.TurtleWorld import *

def draw_pie(t, n, r):
    """Draws a pie
    """
    polypie(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)

    
def polypie(t, n, r):
    """Draws a pie divided into radial segments.
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.
    """
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
pu(bob)
bk(bob, 130)
pd(bob)

# draw polypies
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)
die(bob)

world.canvas.dump()

wait_for_user()
