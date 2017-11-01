import math
x,y = input("Insert two values separated by comma:").split(",")
print("{:10d}".format(x//y))
print("{:10d}".format(x%y))
print("{:10.5f}".format(math.log(x,y)))
print("{:10.5f}".format(math.sqrt(x)))
print("{:10.5f}".format(math.exp(x)))
