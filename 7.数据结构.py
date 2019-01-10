#!/usr/bin/python
'''
数据结构基本上就是——它们是可以处理一些 数据 的 结构 。
或者说，它们是用来存储一组相关数据的。
在Python中有三种内建的数据结构——列表、元组和字典。
'''

# 1. 列表 list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist),'items to purchase.')
print('These items are:')
for item in shoplist:
    print(item, end=' ')# end=' '消除print默认加的换行符
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)

# 2. 元组
'''
元组和列表十分类似，只不过元组和字符串一样是 不可变的 即你不能修改元组。元组通过圆
括号中用逗号分割的项目定义。元组通常用在使语句或用户定义的函数能够安全地采用一组值
的时候，即被使用的元组的值不会改变。
'''
zoo = ('wolf', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = ('monkey', 'dolphin', zoo)
print('Number of animals in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
# 元组最常用的用法是子啊打印语句中
age = 22
name = 'limeiyang'
print("%s is %d years old"%(name,age))
print("why is %s playing with that pathon?"%name)

# 3. 字典
'''
字典类似于你通过联系人名字查找地址和联系人详细情况的地址簿，即，我们把键（名字）和
值（详细情况）联系在一起。注意，键必须是唯一的，就像如果有两个人恰巧同名的话，你无
法找到正确的信息。
注意，你只能使用不可变的对象（比如字符串）来作为字典的键，但是你可以把不可变或可变
的对象作为字典的值。基本说来就是，你应该只使用简单的对象作为键。
键值对在字典中以这样的方式标记：d = {key1 : value1, key2 : value2 }。注意它们的键/值对用冒
号分割，而各个对用逗号分割，所有这些都包括在花括号中。
记住字典中的键/值对是没有顺序的。如果你想要一个特定的顺序，那么你应该在使用前自己
对它们排序。
字典是dict类的实例/对象。
'''
ab = { 'Swaroop' : 'swaroopch@byteofpython.info',
       'Larry' : 'larry@wall.org',
       'Matsumoto' : 'matz@ruby-lang.org',
       'Spammer' : 'spammer@hotmail.com'
       }
print("Swaroop's address is %s" % ab['Swaroop'])
# 添加一个键/值
ab['Guido'] = 'guido@python.org'
# 删除一个键/值
del ab['Spammer']
print('\nThere are %d contacts in the address-book\n' % len(ab))
for name, address in ab.items():
    print('Contact %s at %s' % (name, address))
if 'Guido' in ab:
    print("\nGuido's address is %s" % ab['Guido'])

# 4. 序列
# 列表、元组和字符串都是序列
shoplist = ['apple', 'mango', 'carrot', 'banana']
# 索引操作
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
# 切片操作
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
# 对一个字符串切片操作
name = 'swaroop'
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# 5. 引用
'''
当你创建一个对象并给它赋一个变量的时候，这个变量仅仅 引用 那个对象，而不是表示这个
对象本身！也就是说，变量名指向你计算机中存储那个对象的内存。这被称作名称到对象的绑
定。
'''
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object
print('Copy by making a full slice')
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item
print('shoplist is', shoplist)
print('mylist is', mylist)
# notice that now the two lists are different
'''
注：
如果你想要复制一个列表或者类似的序
列或者其他复杂的对象（不是如整数那样的简单 对象 ），那么你必须使用切片操作符来取得
拷贝。如果你只是想要使用另一个变量名，两个名称都 引用 同一个对象，那么如果你不小心
的话，可能会引来各种麻烦。
'''

# 6. 更多字符串的内容
'''
startwith方法是用来测试字符串是否以给定字符串开
始。in操作符用来检验一个给定字符串是否为另一个字符串的一部分。
find方法用来找出给定字符串在另一个字符串中的位置，或者返回-1以表示找不到子字符串。
str类也有以一个作为分隔符的字符串join序列的项目的整洁的方法，它返回一个生成的大字符串。
'''
name = 'Swaroop' # This is a string object
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))