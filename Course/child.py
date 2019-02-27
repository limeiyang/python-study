
from Case01.father import Father
from Case01.mother import Mother
class Child(Mother,Father):
    # Child Father Mother
    # def __init__(self):
    #     pass
    def __init__(self,earnmoney,playmoney,money):
        self.money = money;
        print("调用母亲的构造函数")
        # super调用父类的构造函数，用于给父类设置属性
        super(Child,self).__init__(playmoney=playmoney)
        super(Mother,self).__init__(earnmoney);
        pass
    def getmoney(self):
        return self.playmoney
        pass
    pass

# 实例化：
child_01 = Child(100,200,90);
child_01.earnMoney()
child_01.playMoney()
print(child_01.playmoney)
print(child_01.earnmoney)
print(child_01.money)
