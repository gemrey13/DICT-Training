def calculate_area(length: float, width: float):
    area = length * width
    return area

length = float(input("Enter length >> "))
width = float(input("Enter width >> "))

print(calculate_area(length, width))
