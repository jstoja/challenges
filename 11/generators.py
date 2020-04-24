"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""
import glob
from collections import Counter
from typing import Iterator
import re

def gen_files(path: str) -> Iterator[str]:
    for f in glob.glob(path):
        yield f

def gen_lines(files: Iterator[str]) -> Iterator[str]:
    for file_name in files:
        with open(file_name, "r") as f:
            for l in f:
                yield l

def gen_grep(lines: Iterator[str], pattern: str) -> Iterator[str]:
    for line in lines:
        if re.match(pattern, line):
            yield line.split()[1]

def gen_count(lines: Iterator[str]) -> Iterator[str]:
    c = Counter(lines)
    for count in c.most_common():
        yield "{} {}".format(count[1], count[0])


if __name__ == "__main__":
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    match = gen_grep(lines, "^import ")
    counts = gen_count(match)
    for c in counts:
        print(c)
