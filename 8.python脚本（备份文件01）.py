#!/usr/bin/python
'''
文件创建备份的程序：

1. 需要备份的文件和目录由一个列表指定。
2. 备份应该保存在主备份目录中。
3. 文件备份成一个zip文件。
4. zip存档的名称是当前的日期和时间。
5. 我们使用标准的zip命令，它通常默认地随Linux/Unix发行版提供。Windows用户可以使
用Info-Zip程序。注意你可以使用任何地存档命令，只要它有命令行界面就可以了，那
样的话我们可以从我们的脚本中传递参数给它。
'''
# 开始
import os
import time
import zipfile

filename = r'F:\backuptest\work'
z = zipfile.ZipFile(filename, 'r')
print(z.read(z.namelist()[0]))

# 权限报错 ！！！！！！！！！！！！！！！！！！！！！！！！待解决
'''
# 1. The files and directories to be backed up are specified in a list.
source = [r'F:\backuptest\work', r'F:\backuptest\work1']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory
target_dir = r'F:\backuptest\work2'# Remember to change this to what you will be using
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')

'''
