#coding=utf-8

def add(a, b):
    print "ADDING %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" %(a, b)
    return a / b

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "===================="
print "Age: %d, \nHeight: %d, \nWeight: %d, \nIQ: %d" % (age, height, weight, iq)
print "===================="
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "age + height - weight * iq / 2 = %d" %what
