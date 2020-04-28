import os

curDir = os.getcwd()

print(curDir)
# os.mkdir('os-folder-from-python')

import time
time.sleep(2)

# os.rename('os-folder-from-python', 'renamed-dir')

os.rmdir('renamed-dir')