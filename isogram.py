def is_isogram(string):
    string2 = ''
    if string == '':
        return True
    for i in string.lower():
        if i in string2 and i != ' ' and i != '-':
            return False
        string2 += i
    else:
        return True