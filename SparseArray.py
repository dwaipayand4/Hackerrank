import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    ns=len(strings)
    nq=len(queries)
    list1=[]
    for i in range(0,nq):
        c=0
        for j in range(0,ns):
            if((queries[i])==strings[j]):
                c=c+1
        list1.append(c)
    return(list1)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
