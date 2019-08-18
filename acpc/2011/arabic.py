import re

pattern = re.compile('([#\s]*)([a-z]*)([#\s]*)')

def fix_line(line):
    l, e, r = pattern.match(line).groups()
    # print("L"+l+"E"+e+"R"+r+".")
    if (l=='' and r=='') or (e=='' and r==''):
        return line
    if r!='': r = r.lstrip() + " "
    if l!='': l = " " + l.rstrip()
    return r+e+l

with open('arabic.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        _ = f.readline().strip()
        line = f.readline().strip()
        fixed_line = fix_line(line)
        print(fixed_line)
