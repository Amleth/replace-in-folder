import glob
import os
import sys

dir = os.path.abspath(sys.argv[1])
dir_target = os.path.join(os.path.dirname(dir), sys.argv[1] + "_new")
os.mkdir(dir_target)

print()
print(f"FROM {dir}")
print(f"TO   {dir_target}")
print()

replacementList = []
replacementList.append(['" "', '""'])
replacementList.append(["PL", 'PN'])
replacementList.append(["on weak beat", 'NA'])
replacementList.append(["IS:IO", 'IO;IS'])
replacementList.append(["IS;IO", 'IO;IS'])

for source_file in glob.glob(f"{dir}/*.xml"):
  target_file = os.path.join(dir_target, os.path.basename(source_file))
  print(f"  🐢 {target_file}")
  with open(source_file) as f:
    with open(target_file, 'w+') as tf:
      for line in f:
        new_line = line
        for r in replacementList:
          new_line = line.replace(r[0], r[1])
        tf.write(f"{new_line}\n")

print()