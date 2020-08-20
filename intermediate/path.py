from pathlib import Path

# -----------------------------------------------------------------

# print(Path.cwd())
# print(Path.home())

# -----------------------------------------------------------------

p = Path('.')
m = [x for x in p.iterdir() if x.is_dir()]

# -----------------------------------------------------------------

n = list(p.glob('**/*.py'))

# -----------------------------------------------------------------

dirt = Path('/algorithms')

# -----------------------------------------------------------------

u = (Path.home() / 'mike.py').is_file()
f = Path.cwd()
t = Path('C:/')
home = Path.home() / 'del.txt'

jpath = Path.home().joinpath('C:/go')

with open(home, 'r') as f:
    read = f.read()

vv = Path.resolve(jpath)
print(vv)
