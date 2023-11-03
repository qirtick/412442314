class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)
point3 = Point3D(7, 8, 9)

print("Значения координат экземпляра point1:", point1.x, ",", point1.y, ",", point1.z)
print("Значения координат экземпляра point2:", point2.x, ",", point2.y, ",", point2.z)
print("Значения координат экземпляра point3:", point3.x, ",", point3.y, ",", point3.z)

Point3D.z = 10

print("Значения координат экземпляра point1:", point1.x, ",", point1.y, ",", point1.z)
print("Значения координат экземпляра point2:", point2.x, ",", point2.y, ",", point2.z)
print("Значения координат экземпляра point3:", point3.x, ",", point3.y, ",", point3.z)

point2.z = 11

print("Значения координат экземпляра point1:", point1.x, ",", point1.y, ",", point1.z)
print("Значения координат экземпляра point2:", point2.x, ",", point2.y, ",", point2.z)
print("Значения координат экземпляра point3:", point3.x, ",", point3.y, ",", point3.z)


###########################################################################################
class Square:
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return self.side * 4


square_1 = Square(5)
area_of_square_1 = square_1.calculate_area()
perimeter_of_square_1 = square_1.calculate_perimeter()
print("площадь квадрата:", area_of_square_1)
print("Периметр квадрата:", perimeter_of_square_1)


###########################################################################################
class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return self.a + self.b + self.get_hypotenuse()

    def get_area(self):
        return 0.5 * self.a * self.b

    def get_hypotenuse(self):
        return (self.a ** 2 + self.b ** 2) ** 0.5


triangle = Triangle(3, 5)

area = triangle.get_area()
perimeter = triangle.get_perimeter()

print("Площадь треугольника:", area)
print("Периметр треугольника:", perimeter)

###########################################################################################\
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Triangle:
    def __init__(self, point_a, point_b, point_c):
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def perimeter(self):
        side_ab = self.point_a.distance_to(self.point_b)
        side_bc = self.point_b.distance_to(self.point_c)
        side_ca = self.point_c.distance_to(self.point_a)
        return side_ab + side_bc + side_ca


point_a = Point(2, 4)
point_b = Point(6, 9)
point_c = Point(6, 0)

triangle = Triangle(point_a, point_b, point_c)
print("Периметр треугольника:", triangle.perimeter())


###########################################################################################

class CPerson:
    def __init__(self, first_name, last_name, middle_name, birth_day, birth_month, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.gender = gender

    def update_information(self, first_name, last_name, middle_name, birth_day, birth_month, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.gender = gender

    def get_information(self):
        return {
            "Имя": self.first_name,
            "Фамилия": self.last_name,
            "Отвество": self.middle_name,
            "день рождения": self.birth_day,
            "месяц рождения": self.birth_month,
            "Год рождения": self.birth_year,
            "Пол": self.gender
        }

    def __del__(self):
        print(f"Удален объект {self.first_name} {self.last_name}")


person = CPerson("Иван", "Иванов", "Иванович", 15, 5, 1990, "Мужской")
print(person.get_information())

person.update_information("Петр", "Петров", "Петрович", 10, 8, 1985, "Мужской")
print(person.get_information())

del person


######################################################################################################
class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def receiveCall(self, name):
        print(f"Звонит {name}")

    def getNumber(self):
        return self.number


phone1 = Phone("123456789", "iPhone X", 150)
phone2 = Phone("987654321", "Samsung Galaxy S10", 170)
phone3 = Phone("111222333", "Google Pixel 3", 160)

print("Phone 1:")
print("Number:", phone1.number)
print("Model:", phone1.model)
print("Weight:", phone1.weight)

print("\nPhone 2:")
print("Number:", phone2.number)
print("Model:", phone2.model)
print("Weight:", phone2.weight)

print("\nPhone 3:")
print("Number:", phone3.number)
print("Model:", phone3.model)
print("Weight:", phone3.weight)

# Вызываем методы для каждого объекта
phone1.receiveCall("John")
phone2.receiveCall("Alice")
phone3.receiveCall("Bob")

print("Phone 1 number:", phone1.getNumber())
print("Phone 2 number:", phone2.getNumber())
print("Phone 3 number:", phone3.getNumber())


###############################################
class Reader:
    def __init__(self, full_name, card_number, faculty, birthdate, phone_number):
        self.full_name = full_name
        self.card_number = card_number
        self.faculty = faculty
        self.birthdate = birthdate
        self.phone_number = phone_number

    def takeBook(self, book_count):
        print(f"{self.full_name} взял {book_count} книги")

    def returnBook(self, book_count):
        print(f"{self.full_name} вернул {book_count} книги")


reader1 = Reader("Петров В. В.", "12345", "Инженерия", "2000-01-01", "+1234567890")
reader1.takeBook(3)
reader1.returnBook(2)