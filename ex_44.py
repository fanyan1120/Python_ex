
class Parent(object):
    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    print "child"
    pass
#coding=utf-8

dad = Parent()
son = Child()
print "============="
print "dad.implicit(): "
dad.implicit()
print "son.implicit():"
son.implicit()


print "============="
class Par(object):
    def override(self):
        print "PARENT override()"

class Chi(Par):
    def override(self):
        print "CHILD override()"

dad = Par()
son = Chi()
dad.override()
son.override()

print "============="
class Parent1(object):
    def altered(self):
        print "PARENT altered()"

class Child1(Parent1):
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child1, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent1()
son = Child1()
dad.altered()
son.altered()
