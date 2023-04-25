

def genString(charNum):
    charNum = int(charNum / 4)
    my_file = open('testString.txt', "w")
    for i in range(charNum):
        char_i = str(1000 + i)
        my_file.write(char_i)
    my_file.close()

def checkString(s):
    my_file = open('testString.txt', "r")
    all_string = my_file.read()
    my_file.close()
    n = all_string.count(s)
    if n > 1:
        print('This String is invalid!')
        return False
    else:
        print('This String is safe!')
        pos = all_string.find(s)
        print('pos: ' + str(pos))
        return True

def findSring(s):
    my_file = open('testString.txt', "r")
    all_string = my_file.read()
    return all_string.find(s)

if __name__ == '__main__':
    # genString(2000)
    checkString('3521')