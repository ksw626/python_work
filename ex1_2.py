#입력하여 해당 단수를 출력

#인풋은 무조건 타이핑한 것을 스트링으로 전환하여 반환한다
#따라서 result = int(number) * value 에서 처음에 int를 빼고 썼을때 스트링과 인트는 연산이 안된다
#인풋은 무조건 타입 지정이 필요하다

number = input('input gugudan ')

print('-------' + number + 'DAN' + '-------')
    
for value in range (1,10):
    result = int(number) * value
    print(str(number) + ' * ' + str(value) + ' = ' + str(result))
