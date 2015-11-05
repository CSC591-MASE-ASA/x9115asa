import math

def dtlz1(x, num_objs, num_decs):
    f = [None]*num_objs

    def gx():
        g = 0.0
        for i in range(0, num_decs-1):
            g += math.pow(x[i] - 0.5, 2) - math.cos(20* math.pi * (x[i] - 0.5))
        g = 100 * (g + num_decs)
        return g

    g = gx()
    f[0] = 0.5 * (1 + g)
    for i in range(0, num_objs-2):
        f[0] *= x[i]

    for i in range(1, num_objs-1):
        f[i] = 0.5 * (1 + g)
        for j in range(0, num_objs-1-(i+1)):
            f[i] *= x[j]
        f[i] *= 1 - x[num_objs - (i + 1)]

    f[num_objs-1] = 0.5 * (1 - x[0]) * (1 + g)

    return f
