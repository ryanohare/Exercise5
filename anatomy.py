
#import sys module
import sys
#retreves the number of command line arguments
argc = len(sys.argv)

# checks if command line arguments is greater than 1 if greater than 1 it will print to many args
if argc > 1:
    print("Too many args")
#if argumnets is less than 1 it will print else statment
else:
    where = "world"
    print("hello", where)
print("goodbye from " + sys.argv[0])




