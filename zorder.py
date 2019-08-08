import sys
import turtle

SCALE = 10
START_OFFSET = 350

def part1by1(n):
    n &= 0x0000ffff
    n = (n | (n << 8)) & 0x00FF00FF
    n = (n | (n << 4)) & 0x0F0F0F0F
    n = (n | (n << 2)) & 0x33333333
    n = (n | (n << 1)) & 0x55555555
    return n


def unpart1by1(n):
    n &= 0x55555555
    n = (n ^ (n >> 1)) & 0x33333333
    n = (n ^ (n >> 2)) & 0x0f0f0f0f
    n = (n ^ (n >> 4)) & 0x00ff00ff
    n = (n ^ (n >> 8)) & 0x0000ffff
    return n


def interleave2(x, y):
    return part1by1(x) | (part1by1(y) << 1)


def deinterleave2(n):
    return unpart1by1(n), unpart1by1(n >> 1)

if __name__ == '__main__':
    turtle.showturtle()
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    for i in xrange(sys.maxint):
        if i > 0:
            turtle.pendown()
        x, y = deinterleave2(i)
        turtle.goto(x * SCALE - START_OFFSET, y * SCALE - START_OFFSET)
