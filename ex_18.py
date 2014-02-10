def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)

def print_one(arg1):
    print "arg1: %r" %arg1

def print_none():
    print "I got nothing."

print_two('print_two_para_1_ss','print_two_para_2_2222')
print_two_again("print_two_again_para_1_4dgvdg","print_two_again_para_2_dgtrt")
print_one("print_one_para_1111111")
print_none()