import os
import sys
import shutil
extensions = ['.xml', '.py', '.sh']
for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        name, extension = os.path.splitext(f)

        if extension in extensions:
            if 'report' not in os.path.basename(name):
                relative_path = os.path.relpath(root, sys.argv[1])
                new_path = os.path.join(sys.argv[2], relative_path)
                os.makedirs(new_path, exist_ok = True)
                print("mkdir {}".format(new_path))
                source = os.path.join(root, f)
                destination = os.path.join(new_path, f)
                shutil.copyfile(source, destination)
                
                print("copyfile {} {}".format(source, destination))
