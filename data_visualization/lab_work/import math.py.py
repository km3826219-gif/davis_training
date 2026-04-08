import math

# 🔹 Cube
def cube_csa(a):
    return 4 * a * a

def cube_tsa(a):
    return 6 * a * a

def cube_volume(a):
    return a ** 3


# 🔹 Cuboid
def cuboid_csa(l, b, h):
    return 2 * h * (l + b)

def cuboid_tsa(l, b, h):
    return 2 * (l*b + b*h + h*l)

def cuboid_volume(l, b, h):
    return l * b * h


# 🔹 Cylinder
def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (h + r)

def cylinder_volume(r, h):
    return math.pi * r * r * h


# 🔹 Cone
def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (l + r)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h


# 🔹 Sphere
def sphere_csa(r):
    return 4 * math.pi * r * r

def sphere_tsa(r):
    return 4 * math.pi * r * r

def sphere_volume(r):
    return (4/3) * math.pi * r ** 3


# 🔹 Hemisphere
def hemisphere_csa(r):
    return 2 * math.pi * r * r

def hemisphere_tsa(r):
    return 3 * math.pi * r * r

def hemisphere_volume(r):
    return (2/3) * math.pi * r ** 3