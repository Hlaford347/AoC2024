import collections

def main():

  input_array_left = []
  input_array_right = []

  with open('day1.txt') as f:
    for index, line in enumerate(f):
      input_array_left.append(int(line.strip().split(" ")[0]))
      input_array_right.append(int(line.strip().split(" ")[-1]))

  input_array_left.sort()
  input_array_right.sort()

  total_distance = 0
  i = 0
  while i < len(input_array_left):
    total_distance += (abs(input_array_left[i] - input_array_right[i]))
    i += 1

  score = 0

  left_freq = collections.Counter(input_array_left)
  right_freq = collections.Counter(input_array_right)
  
  for (key,value) in left_freq.items():
    score += key * value * right_freq[key]
  #print(total_distance)
  print(score)
if __name__ == '__main__':
  main()