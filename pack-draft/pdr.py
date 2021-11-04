import re
from pathlib import Path
from datetime import datetime
from ydk import Ydk, file_to_ydk
import pdb

single_cmd_regex = '^([a-zA-Z]*)$'
arg_cmd_regex = '^([a-zA-Z]*) (.*)$'

def _get_new_fname():
  new_fname = f'{str(datetime.now())}.ydk'
  new_fname = new_fname.replace(' ', '')
  new_fname = new_fname.replace(':', '')
  new_fname = new_fname.replace('-', '')
  new_fname = new_fname.replace('.', '', 1)
  new_fname = new_fname[4:]
  return new_fname

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
    print(f'Adding {pack_name}')
    pack_path: Path = Path(f'./packs/[M] {pack_name}.ydk')
    try:
      new_ydk: Ydk = file_to_ydk(pack_path)
      base = base + new_ydk
    except Exception as e:
      print(f'Error converting [{pack_name}] to object')
      print(e)

  new_name = _get_new_fname()
  new_path = Path('./decks/')
  new_path = new_path / new_name
  with open(new_path, 'w+') as f:
    main_list, extra_list, side_list = base.get_lists()
    
    # write main
    f.write('#created by ...\n#main\n')
    for main_card in main_list:
      f.write(f'{main_card}\n')

    # write extra
    f.write('#extra\n')
    for extra_card in extra_list:
      f.write(f'{extra_card}\n')

    # write side
    f.write('!side\n')
    for side_card in side_list:
      f.write(f'{side_card}\n')
  print(f'Created deck [{new_name}]')
  print(base)

if __name__ == "__main__":
  while True:
    input_cmd = input('>>> ')
    if matches := re.findall(single_cmd_regex, input_cmd):
      if matches[0] == 'quit' or matches[0] == 'exit':
        break
    elif matches := re.findall(arg_cmd_regex, input_cmd):
      matches = matches[0]
      cmd_name = matches[0]
      arg_str = matches[1]
      if cmd_name == 'info':
        info(arg_str)
      elif cmd_name == 'merge':
        merge(arg_str)
    else:
      print(f'>>> [{input_cmd}] unrecognized')

