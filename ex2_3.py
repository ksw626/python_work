#피라미드 반댓변 역순

line = int(input('number: '))

print('------pyramid-----')

for star in range(line,0,-1):
    print(' ' * (line-star) + '*' * star)
    
print('-----end-----')