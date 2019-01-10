#!/usr/bin/python

# 1. 文件
'''
你可以通过创建一个file类的对象来打开一个文件，分别使用file类的read、readline或write方法来
恰当地读写文件。对文件的读写能力依赖于你在打开文件时指定的模式。最后，当你完成对文
件的操作的时候，你调用close方法来告诉Python我们完成了对文件的使用。
'''
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close() # close the file
f = open('poem.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print(line)
# Notice comma to avoid automatic newline added by Python
f.close() # close the file

# 2. 存储器
'''
Python提供一个标准的模块，称为pickle。使用它你可以在一个文件中储存任何Python对象，之
后你又可以把它完整无缺地取出来。这被称为 持久地 储存对象。
还有另一个模块称为cPickle，它的功能和pickle模块完全相同，只不过它是用C语言编写的，因
此要快得多（比pickle快1000倍）。你可以使用它们中的任一个，而我们在这里将使用cPickle模
块。记住，我们把这两个模块都简称为pickle模块。
'''
# import cPickle as p
import pickle as p
shoplistfile = 'shoplist.data'
# the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = open(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()
del shoplist # remove the shoplist
# Read back from the storage
f = open(shoplistfile)
storedlist = p.load(f)
print(storedlist)
# ------------------------------------baocuo