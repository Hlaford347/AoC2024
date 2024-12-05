import re
import time
rege_xmas = r"XMAS"
regex_samx = r"SAMX"
regex_mas = r"MAS"
regex_sam = r"SAM"

def rotate_45_left(list_in,list_ids):
  input_array = list_in
  input_ids = list_ids
  new_text = []
  output_ids = []

  x = len(input_array[0])-1

  while x >= 0:
    new_line = ''
    new_ids = []
    j = 0
    i = x
    while j < len(input_array[0]) and i < len(input_array):
      new_line += input_array[j][i]
      new_ids.append(input_ids[j][i])
      j += 1
      i += 1
    new_text.append(new_line)
    output_ids.append(new_ids)
    x -= 1

  y = 1
  while y < len(input_array):
    new_line = ''
    new_ids = []
    j = y
    i = 0
    while j < len(input_array[0]) and i < len(input_array):
      new_line += input_array[j][i]
      new_ids.append(input_ids[j][i])
      j += 1
      i += 1
    new_text.append(new_line)
    output_ids.append(new_ids)
    y += 1

  return (new_text, output_ids)

def rotate_45_right(list_in, list_ids):
  input_array = list_in
  input_ids = list_ids
  new_text = []
  output_ids = []

  y = 0
  while y < len(input_array[0]):
    new_line = ''
    new_ids = []
    j = y
    i = 0
    while j >=0 and i < len(input_array):
      new_line += input_array[j][i]
      new_ids.append(input_ids[j][i])
      j -= 1
      i += 1
    new_text.append(new_line)
    output_ids.append(new_ids)
    y += 1

  y = len(input_array) - 1
  x = 1
  while x < len(input_array):
    new_line = ''
    new_ids = []
    j = y
    i = x
    while i < len(input_array[0]):
      new_line += input_array[j][i]
      new_ids.append(input_ids[j][i])
      i += 1
      j -= 1
    new_text.append(new_line)
    output_ids.append(new_ids)
    x += 1

  return (new_text,output_ids)

def invert():
  input_array = []
  with open('Day4.txt') as f:
    for index, line in enumerate(f):
      input_array.append(line.strip())
  new_text = []

  y = len(input_array) - 1
  x = 0
  while x < len(input_array[0]):
    new_line = ''
    j = y
    while j >= 0:
      new_line += input_array[j][x]
      j -= 1
    new_text.append(new_line)
    x += 1
  return new_text


def main():

  input_array = []

  with open('day4_angel.txt') as f:
    for index, line in enumerate(f):
      input_array.append(line.strip())

  input_ids = []
  id = 1
  y = 0
  while y < len(input_array):
    input_list = []
    x = 0
    while x < len(input_array[y]):
      input_list.append(id)
      id += 1
      x+= 1
    input_ids.append(input_list)
    y += 1
  sum = 0

  for l in input_array:
    sum += len(re.findall(rege_xmas, l))
    sum += len(re.findall(regex_samx, l))

  for l in invert():
    sum += len(re.findall(rege_xmas, l))
    sum += len(re.findall(regex_samx, l))

  rotate_left_letters, rotate_left_ids  = rotate_45_left(input_array, input_ids)
  rotate_right_letters, rotate_right_ids  = rotate_45_right(input_array, input_ids)

  a = 0
  found_left_ids = []
  for l in rotate_left_letters:
    
    sum += len(re.findall(rege_xmas, l))
    sum += len(re.findall(regex_samx, l))
    matches_mas = re.finditer(regex_mas, l)
    matches_sam = re.finditer(regex_sam, l)
    for m in matches_mas:
      a_loc = m.span()[0] + 1
      found_left_ids.append(rotate_left_ids[a][a_loc])
    for m in matches_sam:
      a_loc = m.span()[0] + 1
      found_left_ids.append(rotate_left_ids[a][a_loc])
    a += 1

  found_right_ids = []
  a = 0
  for l in rotate_right_letters:  
  
    sum += len(re.findall(rege_xmas, l))
    sum += len(re.findall(regex_samx, l))
    matches_mas = re.finditer(regex_mas, l)
    matches_sam = re.finditer(regex_sam, l)
    for m in matches_mas:
      found_right_ids.append(rotate_right_ids[a][m.span()[0] + 1])
    for m in matches_sam:
      found_right_ids.append(rotate_right_ids[a][m.span()[0] + 1])
    a += 1

  print(len(list(set(found_left_ids) & set(found_right_ids))))
  print(sum)
if __name__ == '__main__':
 
  n = time.time()
  main()
  m = time.time()
  print(m-n)