import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = math.sqrt(b**2 - 4*a*c)

sup1 = float(-b + delta)
sup2 = float(-b - delta)

inf = float(2*a)

x1 = float(sup1 / inf)
x2 = float(sup2 / inf)

print("As raízes da {}x² + {}x + {} = 0 são {} e {}".format(a, b, c, x1, x2))
