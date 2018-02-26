print('-----pyramid-----')

for star in range(1,6):
    
#    print(' ' * (range-star) + '*' * star)
#TypeError: unsupported operand type(s) for -: 'type' and 'int'    

    print(' ' * (6 - star) + '*' * star)
    
print('-----end-----')