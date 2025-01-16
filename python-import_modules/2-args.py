#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv

    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc - 1))
    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
