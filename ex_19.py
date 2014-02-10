def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "u have %d cheeses!" % cheese_count
    print "u have %d crackers!" % boxes_of_crackers

print "write numbers without '"
cheese_and_crackers(20, 30)

print "use variables"
cheese = 10
crackers = 50
cheese_and_crackers(cheese, crackers)

print "do math inside"
cheese_and_crackers(5+2, 1111+323)

print "var and math"
cheese_and_crackers(cheese+343, crackers+929)

def get_max_num(num_1, num_2):
    if num_1 >= num_2:
        print "max : %d" %num_1
    else:
        print "max : %d" %num_2

a = 121
b = 62
c = 130
get_max_num(42, c)
get_max_num(422, c)
get_max_num(a+b, c)
get_max_num(b-a, c)
get_max_num(b-a, -100)
get_max_num(c, c)
