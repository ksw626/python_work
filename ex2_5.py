#리얼 피라미드 역순

line = int(input('number: '))

print('------pyramid-----')

for star in range(line,0,-1):
    print(' ' * (line-star) + '*' * (2*star-1))
    
print('-----end-----')