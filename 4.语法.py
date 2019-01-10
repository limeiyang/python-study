print("1.--------------------------")
# 1. if elif else 但是python中没有switch
num01 = 2
if num01 >0:
    print("对")
else:
    print("错")

print("2.--------------------------")
# 2. 累加 while
sum_of_number = 0
input_number = int(input("please input a number:"))
while num01 <= input_number:
    sum_of_number += num01
    num01 += 1
print(sum_of_number)

print("3.--------------------------")
# 3. for的使用 求1到一百累加的和
sum01 = 0
for i in range(1, 101):  # range 取值为[a,b)
    sum01 += i
else:
    print("for还可接else,一个重要的注释是，如果你从"
          "for或while循环中 终止 ，任何对应的循环else块将不执行。")
print("和为", sum01)

print("4.--------------------------")
# 4. range详解
print("range(1,5) 默认步数为1")
for i in range(1, 5):
    print(i)
print("range(1,5,2) 设置步数为2")
for i in range(1, 5, 2):
    print(i)




