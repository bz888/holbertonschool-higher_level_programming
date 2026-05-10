#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    result = 0
    for i in range(argc):
        result += int(sys.argv[i + 1])
    print(result)
