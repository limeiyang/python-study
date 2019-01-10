#!/usr/bin/python

# self
'''
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是
在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本
身，按照惯例它的名称是self。
虽然你可以给这个参数任何名称，但是 强烈建议 你使用self这个名称——其他名称都是不赞成
你使用的。使用一个标准的名称有很多优点——你的程序读者可以迅速识别它，如果使用self
的话，还有些IDE（集成开发环境）也可以帮助你。
给C++/Java/C#程序员的注释
Python中的self等价于C++中的self指针和Java、C#中的this参考。
你一定很奇怪Python如何给self赋值以及为何你不需要给它赋值。举一个例子会使此变得清
晰。假如你有一个类称为MyClass和这个类的一个实例MyObject。当你调用这个对象的方法
MyObject.method(arg1, arg2)的时候，这会由Python自动转为MyClass.method(MyObject, arg1,
arg2)——这就是self的原理了。
这也意味着如果你有一个不需要参数的方法，你还是得给这个方法定义一个self参数。
'''

# 类
# 最简单的类
class myclass:
    pass # pass 不做任何事情，一般用做占位语句。
p = myclass() # 对象/实例 的创建
print(p)

# 对象的方法
'''
我们已经讨论了类/对象可以拥有像函数一样的方法，这些方法与函数的区别只是一个额外的
self变量。现在我们来学习一个例子。
'''
class sayclass:
    def sayhello(self):
        print("hello")
a = sayclass()
a.sayhello()

# __init__ 方法
'''
__init__方法在类的一个对象被建立时，马上运行。这个方法可以用来对你的对象做一些你希
望的 初始化 。注意，这个名称的开始和结尾都是双下划线。
'''
class sayclass01:
    def __init__(self, name):
        self.name = name
    def sayhello(self):
        print("hello, my name is ",self.name)
b = sayclass01('limeiyang') # 实例化时给赋初值
b.sayhello()

# 类与对象的方法
'''
有两种类型的 域 ——类的变量和对象的变量，它们根据是类还是对象 拥有 这个变量而区分。
类的变量 由一个类的所有对象（实例）共享使用。只有一个类变量的拷贝，所以当某个对象
对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。
对象的变量 由类的每个对象/实例拥有。因此每个对象有自己对这个域的一份拷贝，即它们不
是共享的，在同一个类的不同实例中，虽然对象的变量有相同的名称，但是是互不相关的。通
'''
class Person:
    '''Represents a person'''
    population = 0

    def __init__(self, name):
       '''Initializes the person's data.'''
       self.name = name
       print("Initializing %s"%self.name)

       #when this person is created,he/she
       #add to the populathion
       Person.population += 1

    def __del__(self):#  对象的__del__是对象在被gc消除回收的时候起作用的一个方法，它的执行一般也就意味着对象不能够继续引用。
        '''I am dying'''
        print("%s says bye."%self.name)

        Person.population -= 1

        if(Person.population == 0):
            print("I am the last one")
        else:
            print("there are still %d people left."%Person.population)

    def sayHi(self):
        '''Greeting by the person

           Really, that's all it does.
        '''
        print("hi, my name is %s"%self.name)

    def howMany(self):
        '''prints the current population.'''
        if(Person.population == 1):
            print("I am the only person here.")
        else:
            print("we hava %d persons here"%Person.population)

limeiyang = Person("limeiyang")
limeiyang.sayHi()
limeiyang.howMany()

jiaxin = Person("jiaxin")
jiaxin.sayHi()
jiaxin.howMany()

limeiyang.sayHi()
limeiyang.howMany()
'''
Python中所有的类成员（包括数据成员）都是 公共的 ，所有的方法都是 有效的 。
只有一个例外：如果你使用的数据成员名称以 双下划线前缀 比如__privatevar，Python的名称
管理体系会有效地把它作为私有变量。
这样就有一个惯例，如果某个变量只想在类或对象中使用，就应该以单下划线前缀。而其他的
名称都将作为公共的，可以被其他类/对象使用。记住这只是一个惯例，并不是Python所要求
的（与双下划线前缀不同）。
'''

# 继承
'''
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过 继承 机
制。继承完全可以理解成类之间的 类型和子类型 关系。
假设你想要写一个程序来记录学校之中的教师和学生情况。他们有一些共同属性，比如姓名、
年龄和地址。他们也有专有的属性，比如教师的薪水、课程和假期，学生的成绩和学费。
你可以为教师和学生建立两个独立的类来处理它们，但是这样做的话，如果要增加一个新的共
有属性，就意味着要在这两个独立的类中都增加这个属性。这很快就会显得不实用。
一个比较好的方法是创建一个共同的类称为SchoolMember然后让教师和学生的类 继承 这个共
同的类。即它们都是这个类型（类）的子类型，然后我们再为这些子类型添加专有的属性。
使用这种方法有很多优点。如果我们增加/改变了SchoolMember中的任何功能，它会自动地反
映到子类型之中。例如，你要为教师和学生都增加一个新的身份证域，那么你只需简单地把它
加到SchoolMember类中。然而，在一个子类型之中做的改动不会影响到别的子类型。另外一个
优点是你可以把教师和学生对象都作为SchoolMember对象来使用，这在某些场合特别有用，比
如统计学校成员的人数。一个子类型在任何需要父类型的场合可以被替换成父类型，即对象可
以被视作是父类的实例，这种现象被称为多态现象。
另外，我们会发现在 重用 父类的代码的时候，我们无需在不同的类中重复它。而如果我们使
用独立的类的话，我们就不得不这么做了。
在上述的场合中，SchoolMember类被称为 基本类 或 超类 。而Teacher和Student类被称为 导出
类 或 子类 。
'''
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: %s)' % self.name)
    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"' % (self.name, self.age))

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"' % self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "%d"' % self.marks)

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 22, 75)
print # prints a blank line
members = [t, s]
for member in members:
    member.tell() # works for both Teachers and Students

# 