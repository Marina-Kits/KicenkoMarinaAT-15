x = int(input())
print(bin(x)[2:], oct(x)[2:], hex(x)[2:]) if x >= 0 else print("Неверный ввод")