import os
import shutil

root = os.path.dirname(os.path.abspath(__file__))
folder = "Project Outputs for "
extension = ".IntLib"
dest = os.path.join(root, 'libraries')

if not os.path.exists(dest):
    os.makedirs(dest)

itens = os.listdir(root)
dirs = [item for item in itens if os.path.isdir(os.path.join(root, item))]

ignore_dirs = ['.git', 'libraries', '3D Parts']
for ignore in ignore_dirs:
    if ignore in dirs:
        dirs.remove(ignore)

for dir in dirs:
    path = os.path.join(root, dir, f'{folder}{dir}')
    if os.path.exists(path) and os.path.isdir(path):
        ori = os.path.join(path, f'{dir}{extension}')
        if os.path.exists(ori) and os.path.isfile(ori):
            file_dest = os.path.join(dest, f'{dir}{extension}')
            if os.path.exists(file_dest):
                os.remove(file_dest)
            shutil.move(ori, dest)
            print(dir)