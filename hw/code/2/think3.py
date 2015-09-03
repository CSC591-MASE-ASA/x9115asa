#hw2 exercise 1
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."
#hw2 exercise 3
def right_justify(string):
    print ' '*(70-len(string))+string
#hw2 exercise 4
#version 1 of do twice with one argument
def do_twice_1(f):
    f()
    f()
#version 2 of do twice with one argument
def do_twice_2(f, value):
    f(value)
    f(value)
#exercise 3.4 part 5 do_four
def do_four(f, value):
    for i in range(4):
        f(value)
#simple print spam function as shown in exercise

#print spam for part 1
def print_spam():
    print 'spam'
#print spam for part 2
def print_spam2(value):
    print 'spam', value
#print_twice for part 3
def print_twice(input_string):
    print "input: ", input_string+" "+input_string
#print_args for part 5
def print_args(arg):
    print 'value passed: ', arg


#hw2 exercise 3.5
def exercise3_5(n):
    print 'Number of rows and columns: ', n
    for i in range((n-1)*5+1): 
        for j in range((n-1)*5+1):
# Learned something new here bitwise-and is '&' while boolean is (and) 
            if i%5==0 and j%5==0:
                print '+',
            elif j%5==0:
                print '/',
            elif i%5==0:
                print '-',
            else:
                print ' ',
        print

# Main function. Put functions you want to all when script runs here
if __name__ == '__main__':
    print 'Exercise 3.1: '
    repeat_lyrics()
    print
    print 'Exercise 3.3'
    right_justify('allen');
    print 'Exercise 3.4 Part 1: '
    do_twice_1(print_spam)
    print
    print 'Exercise 3.4 Part 2: '
    do_twice_2(print_spam2, 2)
    print
    print 'Exercise 3.4 Part 3 & 4 with modified print_twice'
    do_twice_2(print_twice, 'spam')
    print
    print 'Exercise 3.4 Part 5'
    do_four(print_args, 'example_argument')
    print 'Exercise 3.5 Part 1: '
    exercise3_5(3)
    print
    print 'Exercise 3.5 Part 2: '
    exercise3_5(4)
    
    