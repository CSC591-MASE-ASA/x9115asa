

#hw2 exercise 3.2
def exercise3_5():
    for i in range(11): 
        for j in range(11):
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
    exercise3_5()