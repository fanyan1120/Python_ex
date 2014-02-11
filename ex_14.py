#coding=utf-8

from sys import argv

script, user_name = argv
prompt = ">"

print "Hi %s, I'm the %s script." %(user_name, script)
print "I'd like to ask u a few questions"
print "Do you like me %s ?" %user_name
likes = raw_input(prompt)
print "Where do you live %s" %user_name
lives = raw_input(prompt)
print "What kind of computer do you have?" 
pc = raw_input(prompt)
print """
U said %r about liking me.
U live in %r.
U have s %r computer
""" %(likes, lives, pc)

print "I could join chars u input"
one = raw_input("1st char: ")
two = raw_input("2nd char: ")
three = raw_input("3rd char: ")
four = raw_input("4th char: ")
print "output:\t %r" %one+" "+two+" "+three+" "+four