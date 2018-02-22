#피라미드 응용 (반댓변 피라미드)


#for star in range(1, str(star)):
#TypeError: 'str' object cannot be interpreted as an integer 스트링을 정수로 해석이 안된다?
# 인풋은 항상 스트링으로 전환한다. 그렇다면 이미 스트링상태 숫자로바꿔줄 int를 써본다
"""
for star in range(0, int(star)):
#    empty = ' ' * (str(star) - 1)
#    TypeError: unsupported operand type(s) for -: 'str' and 'int' 이것도 이미 스트링이니 인트로 바꿔본다

#empty = ' ' * (str(star) - 1)로 작동시켰더니
#number: 5
#1
# 2
#  3
#   4
#로 출력됨 벽으로 밀고싶었다.수식의 문제인듯 반대로 되어야할거같다
#게다가 숫자로 나온다
#    empty = ' ' * (int(star))
#    print(empty + str(star))
""" #실패 처음부터 다시해보자 별로바꿔봤자 숫자출력만큼 별만생긴다 ㅎㅎ





line = int(input('number: '))

print('------pyramid-----')

for star in range(1,line+1):
    print(' ' * (line-star) + '*' * star)
    
print('-----end-----')

#진짜 피라미드를 만드려다 반댓변이 되어버림ㅎㅎ 
    