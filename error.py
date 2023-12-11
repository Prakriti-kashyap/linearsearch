try:
    file = open('sample.txt', 'w')
    print('File found!!!')
     
except IOError:
    print('File not found!!!')
