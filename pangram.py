def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetlist = list(alphabet)
    sentencelist= []
    if alphabet == '':
        return False
    else:
        for i in sentence.lower():
            sentencelist.append(i)
        for i in sentencelist:
            if i in alphabetlist:
                alphabetlist.remove(i)
        return alphabetlist == []
print(is_pangram('abcdefghijklmnopqrstuvwxyz'))