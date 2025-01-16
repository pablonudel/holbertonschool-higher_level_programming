#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv

    for i in range(1, argc):
        argv[i] = int(argv[i])
    print(sum(argv[1:]))
