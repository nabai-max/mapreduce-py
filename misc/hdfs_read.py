#!/usr/bin/env python3

import subprocess
import sys


class HdfsReadFile:
    def __init__(self):
        self.count = 0

    def read(self, filename, searchText):
        cat = subprocess.Popen(["hdfs", "dfs", "-cat", filename], stdout=subprocess.PIPE)
        for line in cat.stdout:
            s = line.decode("utf-8")[:-1].split('\t')
            if s[0] == searchText:
                print(s[0], 'occurs', s[1], 'times')
                break


# Main

def main(filename, searchText):
    print(filename)
    hdfsReadFile = HdfsReadFile()
    hdfsReadFile.read(filename, searchText)


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1], sys.argv[2])
