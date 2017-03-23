import random
def grid_creator(r, c):
    return [
        ["{0: >4}".format(str(random.randint(0, 100))) for _ in range(c)]
        for _ in range(r)
    ]
print ('\n'.join(' '.join(row) for row in grid_creator(random.randint(3, 15), random.randint(3, 15))))

