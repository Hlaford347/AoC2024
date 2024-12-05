import re
import time
regex = r"mul\((\d+),(\d+)\)"
do_or_dont_ex = r"(don't\(\)|do\(\))"

def main():

  input_array = []
  sum = 0
  do_dont_index_array = []
  do_or_dont = True
  next_do_dont = 0
  do_dont_array = []

  with open('day3_angel.txt') as g:
    
    do_dont_array = re.finditer(do_or_dont_ex, g.read())

    for do_dont in do_dont_array:
      do_dont_index_array.append({"loc": do_dont.span()[0], "value":re.findall(do_or_dont_ex, do_dont.group())})


  with open('day3_angel.txt') as f:
    input_array = re.finditer(regex,f.read())

    for pair in input_array:

      if next_do_dont < len(do_dont_index_array):
        if pair.span()[0] > do_dont_index_array[next_do_dont]["loc"]:
          do_or_dont = True if do_dont_index_array[next_do_dont]["value"][0] == 'do()' else False
          next_do_dont += 1

      if do_or_dont:
        sum += int(re.findall(regex, pair.group())[0][0]) * int(re.findall(regex, pair.group())[0][1])
        
  print(sum)
if __name__ == '__main__':
  
  n = time.time_ns()
  main()
  m = time.time_ns()
  print(m-n)