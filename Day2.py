def isSafe(diff_list):
  return (all((d > 0) for d in diff_list) or all(d < 0 for d in diff_list)) and all((abs(d) >= 1 and abs(d) <= 3) for d in diff_list)

def makeDiffList(l):
  diff_list = []
  for x, y in zip(l[0::],l[1::]):
    diff_list.append(int(y)-int(x))
  return diff_list

def main():

  input_array = []

  with open('day2_angel.txt') as f:
    for index, line in enumerate(f):
      input_array.append(line.strip().split(" "))
  
  safe = 0
  for l in input_array:
    
    diff_list = makeDiffList(l)
  
    if isSafe(diff_list):
      safe += 1

    else:
      for idx,i in enumerate(l):
        new_list = [ele for index, ele in enumerate(l) if index not in [idx]]
        diff_list = makeDiffList(new_list)
        if isSafe(diff_list):
          safe+=1
          break
    
  print(safe)

if __name__ == '__main__':
  main()