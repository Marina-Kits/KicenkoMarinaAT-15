a=float(input())
digits_for_hex="0123456789ABCDEF"
a_bin=""
a_oct=""
a_hex=""
if a<0 or a!=int(a):
    print("Неверный ввод")
else:
    a2=int(a)
    a8=int(a)
    a16=int(a)
    while a2 > 0:
        a_bin = str(a2 % 2) + a_bin
        a2 = a2 // 2
    while a8 > 0:
        a_oct = str(a8 % 8) + a_oct
        a8 = a8 // 8
    while a16 > 0:
        a_hex = digits_for_hex[a16 % 16] + a_hex
        a16 = a16 // 16
print(a_bin, a_oct, a_hex)
