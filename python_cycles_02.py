import math

numx = 8+8
num = 1


while num < numx + 1:
    print ("{: ^50s}".format('*'*num))

    if num >= numx:
        print("{: ^50s}".format('*'))
        print("{: ^50s}".format('*'))
    else:
        pass

    num = num + 1