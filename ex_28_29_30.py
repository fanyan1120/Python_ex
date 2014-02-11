#coding=utf-8

def print_line(f):
    row = f.readline()
    print "row - ", row
    return row

file_name = "tt.txt"
file = open(file_name)
row1 = print_line(file)
row2 = print_line(file)
if row1 == row2:
    print " row 1 = row 2"
else:
    print "row 1 != row 2"

print "++++++++++++++++"
a = 32
b = 12
if a < b:
    print "a < b"
if a == b:
    print "a = b"
if a > b:
    print "a > b"
	
print "++++++++++++++++"
b += 24
if a < b:
    print "a < b"
else:
    print "a >= b"

print "++++++++++++++++"
b -= 4
if a < b:
    print "a < b"
elif a > b:
    print "a > b"
else:
    print "a = b"