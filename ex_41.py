#coding=utf-8

aaa = ['three', 'two', 'one', 'go!']
print ', '.join(aaa)

print "="*10

class TheThing(object):
    def __init__(self):
        self.number = 0
    
    def some_function(self):
        print "I got called."

    def add_me_up(self, more):
        self.number += more
        return self.number

a = TheThing()
b = TheThing()
a.some_function()
b.some_function()
print "a - ", a.add_me_up(20)
print "b - ", b.add_me_up(30)
print "a - ", a.number
print "b - ",b.number

print "="*10

class TheMultiplier(object):
    def __init__(self, base):
        self.base = base

    def do_it(self, m):
        return m * self.base

x = TheMultiplier(a.number)
print " a.number = ", a.number
print " x = ", x
print x.do_it(b.number)
