#입력하여 해당 단수를 출력

number = input('number: ')

print('-------' + number + 'DAN' + '-------')
    
for value in range (1,10):
    result = int(number) * value
    print(str(number) + ' * ' + str(value) + ' = ' + str(result))