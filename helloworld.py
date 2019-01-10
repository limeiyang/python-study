print("你好 世界")

# 单行解释
'''多行注释'''
"""多行注释"""
'''
python里面单引号和双引号作用一样
pycharm中注释快捷和sublime中一样 ctrl+/
'''


'''
函数编辑
实现加法
~~~~~~~~~~~~~~~~~~
add(num0, num1)--实现两数相加
'''
def add(num0 , num1):
    return  num0 + num1

# 调用add函数
print('100+200=',add(100,200))

# main函数 （也是程序的执行开始）
if __name__ == "__main__":
    print("main 函数的执行")
