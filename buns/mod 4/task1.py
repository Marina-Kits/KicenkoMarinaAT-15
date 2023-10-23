def comparing_numbers(numbers):
    if len(set(numbers))==len(numbers):
        print("Все числа разные")
    elif len(set(numbers))==1:
        print("Все числа равны")
    else:
        print("Есть равные и неравные числа")
comparing_numbers([1,2,3,4])
comparing_numbers([1,1,4,4])
comparing_numbers([1,1,1,1])
