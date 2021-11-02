import re
from pathlib import Path
from ydk import Ydk

single_cmd_regex = '^([a-zA-Z]*)$'
arg_cmd_regex = '^([a-zA-Z]*) (.*)$'

def info(args: str):
  pack_name = args.split()[0]
  packs_path = Path(f'./packs/{pack_name}/about.txt')
  try:
    with open(packs_path) as f:
      for line in f:
        print(line)
  except:
    print(f'Pack [{pack_name}] not found')

def merge(args: str):
  base = Ydk([], [], [])
  pack_names = args.split()
  for pack_name in pack_names:
    pass

  new_name = 'asd.ydk'
  with open(new_name, 'w+'):
    pass

if __name__ == "__main__":
  while True:
    input_cmd = input('>>>')
    if matches := re.findall(single_cmd_regex, input_cmd):
      if matches[0] == 'quit' or matches[0] == 'exit':
        break
    elif matches := re.findall(arg_cmd_regex, input_cmd):
      matches = matches[0]
      cmd_name = matches[0]
      arg_str = matches[1]
      if cmd_name == 'info':
        info(arg_str)
    else:
      print(f'>>> [{input_cmd}] unrecognized')

