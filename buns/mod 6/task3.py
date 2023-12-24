def get_armstrong_numbers():
    for num in range(153, 100000):
        order = len(str(num))
        sum_of_digits = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum_of_digits += digit ** order
            temp //= 10
        if num == sum_of_digits:
            yield num
for i in range(8):
    print(get_armstrong_numbers(), end=' ')
