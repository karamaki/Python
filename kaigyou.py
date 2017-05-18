#!/usr/bin/env python
""" delete_null_lines.py                 (2008/07/02)
    Deleting null lines in a file
"""
datafile = 'nikkei_tech_t.txt'
savefile = 'nikkei_tech__.txt'
input = open(datafile, 'r')
output = open(savefile, 'w')

L = input.readlines()
input.close()

for s in range(len(L)):
  if L[s] != '\n':
    #print(s, L[s])
    output.write(L[s])

output.close()
