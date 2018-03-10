def roof():

    try:
        
        while True:
        
            num = input('입력: ')
            
            number = "1234567890056798776556543211234876590"

            list(number)
                
            count = 0
            
            if int(num) > 10:
                print('한자리 정수를 입력해주세요.')
                continue
            
            for random_number in number:
                    
                if random_number == num:
                    count += 1
                        
            print('출력:', count)
                
    except:
        print('한자리 정수를 입력해주세요')
        roof()
        
roof()