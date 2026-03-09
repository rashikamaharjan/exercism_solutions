def is_armstrong(number):
    count= len(str(number))
    backup = number
    armstrong = 0
    while backup != 0:
        rem = backup % 10
        armstrong = armstrong + rem ** count
        backup = backup / 10
    if armstrong == number :
        return True
    else:
        return False
print(is_armstrong(45))
