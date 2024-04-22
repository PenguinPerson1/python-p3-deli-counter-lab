def line (line):
  if len(line) == 0:
    print('The line is currently empty.')
  else:
    print("The line is currently:",end="")
    for i in range(len(line)) :
      print(f' {i+1}. {line[i]}',end="")
    print("")

def take_a_number(line:list,name:str):
  line.append(name)
  print(f"Welcome, {name}. You are number {len(line)} in line.")

def now_serving(line):
  if len(line) == 0:
    print("There is nobody waiting to be served!")
  else:
    print(f"Currently serving {line.pop(0)}.")