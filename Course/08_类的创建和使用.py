
#【1】===创建类并使用====
class Person():
    # 属性
    name = "盲僧"
    age = 18;
    def __init__(self,name,age):
        print("====构造函数调用：init=======")
        self.name = name;
        self.age = age;
        pass
    # self:表示类本身
    # 设置名称
    def SetName(self,name):
        self.name = name;
        pass
    def GetName(self):
        return self.name
        pass
    # 输入语句
    def greet(self):
        print("欢迎%s来到王者峡谷!!!"%self.name)
        pass
    pass
# 类的实例化 java ：Person person = new Person();
# person = Person();
# person.greet()
# # 设置姓名
# person.SetName("亚索")
# person.greet()
# # 获取name
# print(person.GetName())

# 构造函数的使用
person_01 = Person("荆轲",18);
person_01.greet();













