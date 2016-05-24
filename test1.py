def find(x):
    y=1.0
    #此处关键，一定要写1.0，这样才是浮点型，否则是整形，会一直循环2 
    while abs(y*y-x)>1e-6:
        # print abs(y*y-x)
        y=(y+x/y)/2
        print y
    print "last:%s"%y

if __name__ == '__main__':
    find(5)