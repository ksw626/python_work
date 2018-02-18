#구구단을 1단부터 9단까지 출력

for dan in range (1,10):
    print('-------' + str(dan) + 'DAN' + '-------')
    
    for value in range (1,10):
        result = dan * value
        print(str(dan) + ' * ' + str(value) + ' = ' + str(result))
