def get_cuboid_volume(h):
    def volume(l, b):
        return l * b * h
    return volume


volume_height_10 = get_cuboid_volume(10)
cuboid_volume = volume_height_10(5, 4)
print(f"Cuboid (5 ,4, 10) volume is {cuboid_volume}")


def add_number(a, b):
    def multiply(c):
        return c * (a + b)
    return multiply


result = add_number(2, 3)
multiply = result(10)
print(multiply)

print("letsgo")
print("letsgo2")
