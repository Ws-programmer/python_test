# -*-coding:utf-8-*-

"""
第一个python类，学习各个基础类型
"""

# 字符串相关测试：https://www.runoob.com/python/python-strings.html
def test_str(string):
    length = len(string)
    if length < 0:
        return
    print("入参为一个字符串：" + string)

    print("字符串截取一部分：" + string[0: length - 1])
    print("字符串里的字符也是一个字符串: %s ，没有类似java的char：%s", string[0],  type(string[0]))
    # 判断字符a在不在字符串中
    if "a" in string:
        print("a在string")
    # find和index类似，但是index不在会报错，而find只会-1
    print("判断字符a的位置：%s", string.find("a"))
    try:
        print("判断字符a的位置：%s", string.index("a"))
    except:
        print("发现异常：")
    print("每个字符件增加‘b’字符’: %s", string.join("b"))





def main():
    # python 中的输入是print()函数
    # string = input()
    string = "1,2,3,4,5"
    test_str(string)
    array = string.split(",")
    # print(type(array))
    # print(array)
    # yuanzu = (tuple)(array)
    # print(type(yuanzu))
    # print(12345)
    


if __name__ == '__main__':
    main()