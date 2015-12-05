import math

def dtlz1(x, num_objs, num_decs):
    f = [None]*num_objs

    def gx():
        g = 0.0
        for i in range(0, num_decs):
            g += math.pow(x[i] - 0.5, 2) - math.cos(20* math.pi * (x[i] - 0.5))
        g = 100 * (g + num_decs)
        return g

    g = gx()
    f[0] = 0.5 * (1 + g)
    for i in xrange(num_objs-1):
        f[0] *= x[i]

    for i in xrange(1, num_objs-1):
        f[i] = 0.5 * (1 + g)
        for j in range(0, num_objs-(i+1)):
            f[i] *= x[j]
        f[i] *= 1 - x[num_objs - (i + 1)]

    f[num_objs-1] = 0.5 * (1 - x[0]) * (1 + g)
    return f

def dtlz3(x, num_objs, num_decs):
    f = [None]*num_objs

    def gx():
        g = 0.0
        for i in xrange(num_decs):
            g += math.pow(x[i] - 0.5, 2) - math.cos(20* math.pi * (x[i] - 0.5))
        g = 100 * (g + num_decs)
        return g

    g = gx()
    f[0] = 1 + g
    for i in xrange(num_objs-1):
        f[0] *= math.cos(x[i]*math.pi/2)

    for i in xrange(1, num_objs-1):
        f[i] = 1 + g
        for j in xrange(num_objs - (i+1)):
            f[i] *= math.cos(x[j]*math.pi/2)
        f[i] *= math.sin(x[num_objs - (i+1)] * math.pi/2)

    f[num_objs-1] = (1 + g) * math.sin(x[0] * math.pi/2)

    return f

def dtlz5(x, num_objs, num_decs):
    theta = [None]*num_objs
    f = [None]*num_objs

    def gx():
        y = 0.0
        for i in range(0, num_decs):
            y += math.pow(x[i]-0.5, 2)

        return y

    g = gx()
    t = 0.0
    theta[0] = x[0]
    t = 1/(2*(1+g))

    for i in xrange(1, num_objs):
        theta[i] = t + ((g*x[i])/(1+g))

    f[0] = 1 + g
    for i in xrange(num_objs-1):
        f[0] *= math.cos(theta[i] * math.pi/2)

    for i in xrange(1, num_objs-1):
        f[i] = 1 + g
        for j in xrange(num_objs - (i+1)):
            f[i] *= math.cos(theta[j] * math.pi/2)
        f[i] *= math.sin(theta[num_objs-(i+1)]*math.pi/2)

    f[num_objs-1] = (1 + g)*math.sin(theta[0]*math.pi/2)

    return f

def dtlz7(x, num_objs, num_decs):
    f = [None]*num_objs

    def gx():
        y = 0.0
        for i in xrange(num_decs):
            y += x[i]
        return (9*y/num_decs)

    def hx(f, g):
        y = 0.0
        for i in xrange(num_objs-1):
            y += (f[i] / (1 + g)) * (1 + math.sin(3*math.pi*f[i]))
        return num_objs - y

    g = 1 + gx()

    for i in xrange(num_objs-1):
        f[i]=x[i]

    f[num_objs-1] = (1+g)*hx(f, g)

    return f
