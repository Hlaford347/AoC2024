import re
import collections
import time

def create_ordered_rules(rules):
  ordered_rules = {}
  left = []
  right = []
  for rule in rules:
    left.append(rule.split("|")[0])
    right.append(rule.split("|")[1])
  
  for idx,r in enumerate(right):
    if ordered_rules.get(str(r)) is None:
      ordered_rules[str(r)] = [left[int(idx)]]
    else:
      ordered_rules.get(str(r)).append(left[int(idx)])
  
  return ordered_rules

def sort_rule(s_list, ordered_rules):
  sorted_list = []
  target_length = len(s_list)
  working_list = s_list[:]
  while len(sorted_list) < target_length:
    for x in working_list:
      test = [y for y in working_list if y != x]
      valid = True
      for t in test:
        o_r = ordered_rules.get(str(t)) if ordered_rules.get(str(t)) is not None else []
        if x in o_r:
          valid = False

      if valid:
        working_list.remove(x)
        sorted_list.append(x)

  return sorted_list

def main():

  input_array = []
  rules_array = []

  with open('day5_angel.txt') as f:
    for index, line in enumerate(f):
      input_array.append(line.strip())

  stop_index = 0
  for idx,l in enumerate(input_array):
    if l == '':
      stop_index = idx
      break
    else:
      rules_array.append(l)
  ordered_rules = create_ordered_rules(rules_array)

  update_array = input_array[stop_index+1:]
  update_list = []
  for u in update_array:
    update_list.append(u.split(","))

  sum = 0
  for u in update_list:
    x = 0
    valid = True
    while x < len(u) and valid:
      y = x
      while y < len(u) and valid:
        o_r = ordered_rules.get(str(u[x])) if ordered_rules.get(str(u[x])) is not None else []
        if u[y] in o_r:
          valid = False
          break
        
        y += 1
      x += 1
    
    if not valid:
      s = sort_rule(u, ordered_rules)
      sum += int(s[int((len(s) - 1) / 2)])
      
  print(sum)

if __name__ == '__main__':
 
  n = time.time()
  main()
  m = time.time()
  print(m-n)