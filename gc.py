#!/usr/bin/pypy

import sys

best_name = ""
best_value = 0.0

cur_string = ""
cur_name = ""

def update(string, name):
  if len(string) == 0:
    return best_value, best_name
  cur_value = (string.count("C") + string.count("G")) / float(len(string))
  if cur_value - best_value > 0.000001:
    return cur_value, name[1:]
  return best_value, best_name

for line in sys.stdin:
  if line.startswith('>'):
    best_value, best_name = update(cur_string, cur_name)
    cur_name = line.strip()
    cur_string = ""
  else:
    cur_string += line.strip()

best_value, best_name = update(cur_string, cur_name)

print best_name + "\n" + str(best_value * 100)
