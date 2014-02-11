#coding=utf-8

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "num %d" % number

for fruit in fruits:
    print "fruit - %s" % fruit

for i in change:
    print "got %r" % i

elements = []
for i in range(0, 6):
    print "adding %d to elements" % i
    elements.append(i)

for i in elements:
    print "element - %d" % i

ele = range(0, 6)
for i in ele:
    print "ele - %d" % i

#array_two = [[1,2,3],[4,5,6]]
#for i in array_two:
#    print "array_two - %d" % i
