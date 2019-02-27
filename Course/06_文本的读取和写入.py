
# 【1】====文本的读取====
# 第一个参数：打开文件的路径
# 第二个参数：读写权限 :r表示只读 w表示写入 a表示追加
# 第三个参数：模式：1 = 缓存和 0 不缓存 默认情况下：缓存
# 打开文件
file = open("C:\/Users\/Administrator\/Desktop\/123.txt","r",1);
# 读取文件
print(file.read())
# 关闭文件
file.close()
# 写入数据
# 当文本不存储的时候会自动创建
# w写入会代替原有的文件内容
file_01 = open("C:\/Users\/Administrator\/Desktop\/abc.txt","a",1,encoding="utf-8");
file_01.write("2019年2月27日\n武汉工程大学 \n2019-2-27 11:18:43 Python实训 ")
file_01.close()
file_02 = open("date/2019年2月27日.txt","w",1,encoding="utf-8");

