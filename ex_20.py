from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(row_num, f):
    print row_num, f.readline()

current_file = open(input_file)
print "==========whole file=========="
print_all(current_file)

print "==========rewind=========="
rewind(current_file)

print "==========three lines=========="
line = 1
print "print line %d" %line
print_a_line(line, current_file)
line += 1
print "print line %d" %line
print_a_line(line, current_file)
line += 1
print "print line %d" %line
print_a_line(line, current_file)
