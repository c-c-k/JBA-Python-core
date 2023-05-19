import os
import time
import subprocess

print('aaa')
time.sleep(3)
# os.system('clear' if os.name == 'posix' else 'cls')
# NOTE: python documentation suggests always preferring subprocess to os.
subprocess.call('clear' if os.name == 'posix' else 'cls')
print('bbb')

