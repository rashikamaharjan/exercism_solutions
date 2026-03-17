def square_root(number):
    for i in range(1, number+1):
        if number / i == i and number % i == 0:
            return i
print(square_root(1))