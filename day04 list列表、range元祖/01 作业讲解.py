# # for i in 'afdsf':
# #     print(i)
#
# # break continue
# # s1 = 'fsdafsda'
# # for i in s1:
# #     continue
# #     print(i)
#
# Day03作业及默写
#
# 有变量name = "aleX leNb" 完成如下操作：

name = "aleX leNb"

# 移除 name 变量对应的值两边的空格,并输出处理结果
# strip = name.strip()
# print(strip)
# 判断 name 变量是否以 "al" 开头,并输出结果
# if name.startswith("al"):
#     print(name)
# 判断name变量是否以"Nb"结尾,并输出结果
#
# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果

# replace = name.replace("l", "p")
# print(replace)
# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
#方法1
# index = name.index("l")
# target = name[0:index] +"p"+name[index+1:]
# print(target)
# 方法2
# target2 = name.replace("l", "p", 1)
# print(target2)
# 将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
# split = name.split("l")
# print(split)
# 将name变量对应的值根据第一个"l"分割,并输出结果。
# split = name.split("l", 1)
# print(split)
# 将 name 变量对应的值变大写,并输出结果
# upper = name.upper()
# print(upper)
# 将 name 变量对应的值变小写,并输出结果
# lower = name.lower()
# print(lower)
# 判断name变量对应的值字母"l"出现几次，并输出结果
# print(len(name) - len(name.replace("l","")))
# 如果判断name变量对应的值前四位"l"出现几次,并输出结果
# name = name[0:4]
# print(len(name) - len(name.replace("l","")))
# 请输出 name 变量对应的值的第 2 个字符?
#
# 请输出 name 变量对应的值的前 3 个字符?
#
# 请输出 name 变量对应的值的后 2 个字符?
#
# 2.有字符串s = "123a4b5c"
s = "123a4b5c"
# 通过对s切片形成新的字符串s1,s1 = "123"
# 通过对s切片形成新的字符串s2,s2 = "a4b"
# 通过对s切片形成新的字符串s3,s3 = "1345"
# 通过对s切片形成字符串s4,s4 = "2ab"
# 通过对s切片形成字符串s5,s5 = "c"
# 通过对s切片形成字符串s6,s6 = "ba2"
# 使用while和for循环分别打印字符串s="asdfer"中每个元素。
#
# 使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
# s = "asdfer"
# for i in s:
#    print(s)

# 使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。
# s="abcdefg"
# for i in s:
#     print(i + 'sb')


# 使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = '321'
# for i in s:
#     print('倒计时{}秒'.format(i))
# print(i)
# print('出发！')
# 实现一个整数加法计算器(两个数相加)：
#
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。
#
# 选做题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
#
# 计算用户输入的内容中有几个整数（以个位数为单位）。
# ​ 如：content = input("请输入内容：") # 如fhdal234slfh98769fjdla
#
# 选做题：写代码，完成下列需求：
# 用户可持续输入（用while循环），用户使用的情况：
#
# 输入A，则显示走大路回家，然后在让用户进一步选择：
#
# 是选择公交车，还是步行？
#
# 选择公交车，显示10分钟到家，并退出整个程序。
#
# 选择步行，显示20分钟到家，并退出整个程序。
#
# 输入B，则显示走小路回家，并退出整个程序。
#
# 输入C，则显示绕道回家，然后在让用户进一步选择：
#
# 是选择游戏厅玩会，还是网吧？
#
# 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
#
# 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
#
# 写代码：计算 1 - 2 + 3 ... + 99 中除了88以外所有数的总和？
#
# **选做题：**判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海 ⾃来⽔来⾃海上
#
# 制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进行任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx
