""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:

รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """


def calculate_circle(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    # area = f"{area:.2f}"
    # circumference = f"{circumference:.2f}"
    return {
        "area":round(area,2),
        "circumference":round(circumference,2)
    }
c1 = calculate_circle(2)
print(c1)


def sum(n):
    a = n*5
    b = n +5
    return a,b

a,b=sum(10)
print("a",a)
print("b",b)