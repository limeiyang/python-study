#!/usr/bin/python
import os
#对所有文件以数字递增的方式重命名
##
# 源文件名：01. 准 备 中.mp3
#          02. 给 我一 首 歌的 时 间.mp3
#修改：准备中.mp3
#      给我一首歌的时间.mp3
##
def file_rename():
    i = 0
    #需要重命名的文件绝对路径
    path = r"G:\周杰伦歌曲"
     #读取该文件夹下所有的文件
    filelist = os.listdir(path)
    #遍历所有文件
    for files in filelist:
        i = i + 1
        Olddir = os.path.join(path, files)    #原来的文件路径
        if os.path.isdir(Olddir):       #如果是文件夹则跳过
            continue
        #os.path.splitext(path)  #分割路径，返回路径名和文件扩展名的元组
        #文件名，此处没用到
        filename = os.path.splitext(files)[0]
        #文件扩展名
        filetype = os.path.splitext(files)[1]         #如果你不想改变文件类型的话，使用原始扩展名

        newfilename = filename.strip('0123456789. ')  # 删除数字.和第一个空格
        newfilename = newfilename.replace(' ', '') # 删除空格
        print(newfilename + filetype)
        Newdir = os.path.join(path, newfilename+filetype)   #新的文件路径
        try:
            os.rename(Olddir, Newdir)
        except:
            print("e") # 命名时重复的文件名会直接跳过并抛出e的异常
    return True

if __name__ == '__main__':
    file_rename()
