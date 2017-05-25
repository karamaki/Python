#!/usr/bin/env python
import sys
""" delete_null_lines.py                 (2008/07/02)
    Deleting null lines in a file
"""
argvs = sys.argv
datafile = argvs[1]
savefile = argvs[2]
input = open(datafile, 'r')
output = open(savefile, 'w')

L = input.readlines()
input.close()

for s in range(len(L)):
  if L[s] != '\n':
    #print(s, L[s])
    output.write(L[s])

output.close()
