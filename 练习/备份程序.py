# encoding = utf-8
__author__ = "Ang Li"

import os
import time

source = ['K:\git\python-stu\练习\\test_dir1','K:\git\python-stu\练习\\test_dir2','K:\git\python-stu\练习\\test_dir3']
target = 'K:\git\python-stu\练习\\bak_dir'
if not os.path.exists(target):
    os.mkdir(target)
today = target + os.sep + time.strftime('%Y%m%d')

if not os.path.exists(today):
    os.mkdir(today)
comment = str(input('>>> '))
now = time.strftime('%H%M%S')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + comment + '.zip'
if not os.path.exists(target):
    os.mkdir(target)
    print('backup dir create successful.')

zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


