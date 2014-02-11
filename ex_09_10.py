#coding=utf-8

# ====== ex 09 =======
fruit = "apple pear banana orange"
vegetable = "tomato\ncabbage\tspinach"
print "Girls love ", fruit
print "Popeye loves ", vegetable

print """
line 1.
line 2
I'm typing the 3rd line,
and the 4th line
5th line
...
"""

# ====== ex 10 =======
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fish
\t* Catnip\n\t* Grass
"""
fat_cat_2 = '''
I'll do a list 2:
\t* Cat food
\t* Fish
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat_2

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,s