number = int(input("Введите число"))
edinitsi = number % 10
desyatki = number % 100 // 10
sotni = number % 1000 // 100
tusyachi = number // 1000
print(f"первая цифра {tusyachi} вторая цифра {sotni} третья цифра{desyatki} четвертая цифра {edinitsi}")
