"""
算数运算符
"""


class Vector:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        return Vector(self.x * other)

    def __rmul__(self, other):
        return Vector(self.x * other)

    def __imul__(self, other):
        self.x += other
        return self


v01 = Vector(2)
re = v01 * 3
print(re.x)
vo2 = 6
re1 = 3 * vo2
print(re1)

vo3 = 1
print(id(vo3))
vo3 += 2
print(vo3)
print(id(vo3))

v04 = Vector(1)
print(id(v04))
v04 += 2
print(v04)
print(id(v04))
