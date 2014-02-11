#coding=utf-8

x = "%d green bottles hanging on the wall." %10
apple = "apples"
orange = "oranges"
y = "there are 5 %s and 10 %s on the table." %(apple, orange)
print x
print y
print "I sang the sang: %r " % x
print "I said: '%s' " % y

ff = False
tt = True
joke = "Isn't that joke funny? %r"
print joke % ff
print joke % tt
print joke % x

a = "aaaa"
b = "bbbb"
print a+" join "+b

print "111 222 three four"
print "print %s" % 'string'
print "bala"*5

formatter = "%r - %r - %s - %r"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"today isn't Sunday, today is Monday.",
	"tomorrow is Tuesday",
	"the day after tomorrow is Wednesday 周三",
	x
)

