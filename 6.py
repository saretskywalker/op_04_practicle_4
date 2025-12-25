import math
x_gradus = float(input("Введите грудс угла "))
x_rad = math.radians(x_gradus)
print(f"значение тригонометрического выражения равно {math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad)**2}")
