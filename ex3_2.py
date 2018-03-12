#랜덤 숫자를 출력한다.

import random

while True:
    
    try:
        
        num = input('범위를 지정해주세요: ' + '\n나가려면 quit를 입력해주세요 ')
        num = int(num)
    
        if num == quit:
            break
        
        print(random.randrange(0, int(num)))
        
    except:
        print('잘못된 입력입니다. 정수를 입력해주세요')
        continue