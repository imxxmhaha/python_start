#大小写转换
str1 = "bwm"
print(str1.upper())
print("BWM".lower())
#首个单词字母大写capitalize()
print("how are you!".capitalize())
#所有单词首字母大写title()
print("how are you!".title())


###1格式化字符串
print("{} {} you".format("I","love"))
print("{1} {0} you".format("love","I"))
str2 = "我叫{name},我在{course}班,喜欢{hobby},今年{age},身高{height}".format(hobby = "吃鸡",name="小鸣哥",course = "3-2",age = 18,height="175cm")
print(str2)

###2格式化数字format() 同样支持数字格式化 但是返回值是string类型
param1 = format(1234.89555, "0.2f")  #小数保留2位  四舍五入
print(param1)
param2 = format(123456789, "0,.3f")  #千分位分隔符  123,456,789.000
print(param2)
##2.1在字符串格式化输出时,如遇到要格式化输出的数字,则需要在{}内增加:前缀,之后写上数字格式化语句
print("请您向{}账户转账¥{:0,.3f}元".format("9527",123456789))


###3.制表符与换行符
#制表符 \t
#换行符 \n
table = "姓名\t性别\t年龄\n赵四\t男士\t42"
print(table)
table = """
姓名  性别  年龄
赵四  男士   42
张三  男士   50
莉莉  女士   26
"""
print(table)
#str.lstrip 删除左侧空白
#str.rstrip 删除右侧空白
#str.strip 删除两端空白
print("   hello   ".lstrip())
print("   hello   ".rstrip())
print("   hello   ".strip())


###4.字符串查找与替换
#4.1 str.find函数用于获取子字符串首次出现的位置 若不存在,返回-1 类似于java中的indexOf
#语法:str.find(目标串,[开始位置],[结束位置])
source = "Nice to meet you,i need your help!"
print(source.find("ee"))
print("ee" in source) #True

#4.2 str.replace
#语法:str3.replace(被替换的串,用来替换的串,[替换个数])
str3 = "this is string example...wow!!! this is really string"
pstr3 = str3.replace("is","was")
print(pstr3)
pstr3 = str3.replace("is","was",3)
print(pstr3)
