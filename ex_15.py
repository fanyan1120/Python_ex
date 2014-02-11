#coding=utf-8

from sys import argv

script, filename = argv

txt = open(filename)
print txt.read()

print "Type the file name you want to read, please"
file_name = raw_input("> ")
text = open(file_name)
print text.read()
