from swampy.TurtleWorld import *
from polygon import *

def petal(t, r, angle):
    """Draws a petal
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    """Move Turtle
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

# draw 3 flowers.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

world.canvas.dump()

wait_for_user()
