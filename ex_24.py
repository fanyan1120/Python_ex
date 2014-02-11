#coding=utf-8

print "print ' in \""
print 'print \' in \' \nprint \\, print enter: \n print tab between aaa: aaa\taaa'

aaa = """
\tprint a tab
balabalabala
print enter:\n in a lien
print enter and tab:\n\t\tbala
"""
print "================"
print aaa
print "================"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 400
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 6003
beans, jars, crates = secret_formula(start_point)
print "secret_formula = %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10
print "secret_formula = %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
