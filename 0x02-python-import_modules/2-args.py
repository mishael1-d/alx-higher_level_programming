#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = (len(sys.argv) - 1)
    if(arguments == 0):
        print("0 arguments.")
    elif(arguments > 0):
        if(arguments == 1):
            print("{} argument:".format(arguments))
        else:
            print("{} arguments:".format(arguments))
        for i in range(1, (arguments + 1)):
            print("{}: {}".format(i, sys.argv[i]))\n
