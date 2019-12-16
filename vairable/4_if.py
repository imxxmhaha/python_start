# if 条件语句

'''
初识结构
if 条件:
    执行结果
'''

# 第一种结构:单独if
'''
print(111)

if 3 > 2:
    print(222)
print(333)
'''

# 第二种结构: if else

'''
choice =int(input('请输入你猜的大小:'))

if 0<choice<4 :
    print('你猜的是小')
else:
    print('你猜的是大')
'''

# 第三种结构: 多个条件选一个  if elif elif...else

'''
choice =int(input('请输入你猜的大小:'))

if choice == 3 :
    print('我请你吃饭')
elif choice == 4:
    print('我请你游泳')
elif choice ==5:
    print('我请你唱歌')
else:
    print("这都没猜对,你请我吃饭")
'''

# if 嵌套
username = input("请输入用户名:")
password = input("请输入密码:")
if username == 'alex':
    print(666)
    if password == '123':
        print("密码正确,登录成功")
    else:
        print("密码不正确")

else:
    print("用户名不正确")
