def is_armstrong_number(num):
    power=len(str(num))
    sum_of_powers=sum(int(digit)**power for digit in str(num))
    return num==sum_of_powers

def generator_armstrong_numbers():
    num=10
    while True:
        if is_armstrong_number(num):
            yield num
        num+=1

def get_armstrong_numbers():
    return next(generator)

generator = generator_armstrong_numbers()
for i in range(8):
    print(get_armstrong_numbers(), end=' ')