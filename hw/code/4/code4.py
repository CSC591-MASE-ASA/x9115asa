import random
def schaffer():
    
    lower, upper = -100000, 100000
    x=random.randrange(lower, upper)
    min = max = (x**2+(x-2)**2)
    for i in range(100):
        x = random.randrange(lower, upper)
        f1 = x**2
        f2 = (x-2)**2
        sum = f1+f2
        if sum > max:
            max = sum
        if sum < min:
            min = sum
    return min, max
print schaffer()