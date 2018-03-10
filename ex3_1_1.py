#숫자 1234567890056798776556543211234876590 를 가지고 있는 데이터가 있다.
#유저가 숫자 하나를 입력하면 해당 숫자가 데이터에 몇개가 있는지 알려주도록하자.
number = "1234567890056798776556543211234876590"

while True:

    num = input('입력: ')

    list(number)
        
    count = 0
    
    for random_number in number:
            
        if random_number == num:
            count += 1
                
    print('출력:', count)
