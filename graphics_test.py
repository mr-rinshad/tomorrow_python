# selective import for rectangle and circle
from graphics.graphics_3d.cuboid import cuboid_area, cuboid_peri
from graphics.graphics_3d.sphere import sphere_area, sphere_peri
from graphics.rectangle import area, peri
from graphics.circle import circle_area, circle_peri

# ----- RECTANGLE -----
print("\n--- Rectangle ---")
l = float(input("Enter rectangle length: "))
b = float(input("Enter rectangle breadth: "))
print("Rectangle area =", area(l, b))
print("Rectangle perimeter =", peri(l, b))


# ----- CIRCLE -----
print("\n--- Circle ---")
r = float(input("Enter circle radius: "))
print("Circle area =", circle_area(r))
print("Circle perimeter =", circle_peri(r))


# ----- CUBOID -----
print("\n--- Cuboid ---")
l = float(input("Enter cuboid length: "))
b = float(input("Enter cuboid breadth: "))
h = float(input("Enter cuboid height: "))
print("Cuboid area =", cuboid_area(l, b, h))       # updated
print("Cuboid perimeter =", cuboid_peri(l, b, h))  # updated


# ----- SPHERE -----
print("\n--- Sphere ---")
r = float(input("Enter sphere radius: "))
print("Sphere area =", sphere_area(r))       # updated
print("Sphere perimeter =", sphere_peri(r))  # updated
