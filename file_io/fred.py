#! /usr/bin/python3

import sys


def isPositiveInt(x):
    try:
        i = int(x)
        if i > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def DoIt(alist=None):
    if not alist:
        if len(sys.argv) == 1:
            print("enter more arguments")
            return
        else:
            alist = sys.argv
    fin = open(alist[1], 'r')
    s = fin.read()
    fin.close()
    if '\r\n' in s:
        lines = s.split('\r\n')
    else:
        lines = s.split('\n')
    fout = open(alist[2], 'w')
    for line in lines:
        if line:
            nums = [int(x) for x in line.split(',') if isPositiveInt(x)]
            num = len(nums)
            total = sum(nums)
            fout.write(str(num) + ',' + str(total) + '\n')
    fout.close()
    print("output file", alist[2], "was written to successfully")


def main():
    DoIt()


if __name__ == "__main__":
    main()
