# -*- coding: gbk -*-
import os


def WinUpLoc(loc):  # 以Windows格式返还文件所在的原本目录
    if loc[0] == '''"''':  # 去掉双引号、最后一个反斜杠
        loc = loc[1:-1]
    lis = loc.replace("\\", "/").split('/')
    lis.pop()
    loc = ''
    for ji in range(len(lis)):
        loc = loc + str(lis[ji]) + '/'
    return loc[0:-1].replace("/", "\\")


def Function1():
    fileAdrStr = input("用Demucs分离音频，指定卡拉OK模式。\n输入文件地址，或拖进CMD。\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("接下来转入CMD执行。\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n mdx_extra --two-stems=vocals'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\n执行完毕。")


def Function2():
    fileAdrStr = input("用Demucs分离音频，指定专业音频模式。\n输入文件地址，或拖进CMD。\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("接下来转入CMD执行。\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n mdx_extra'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\n执行完毕。")


def Function4():
    fileAdrStr = input("用Demucs分离音频，指定高性能专业音频模式。\n输入文件地址，或拖进CMD。\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("接下来转入CMD执行。\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n htdemucs'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\n执行完毕。")


def Function3():
    fileAdrStr = input("用Demucs分离音频，指定高性能专业音频模式。\n输入文件地址，或拖进CMD。\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("接下来转入CMD执行。\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n htdemucs --two-stems=vocals'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\n执行完毕。")


def FunctionInput():
    global inp
    inp = input("-选择分离模式：\n"
                "-1-卡拉OK模式，单独分离人声。mdx_extra\n"
                "-2-专业音频模式，分离4个轨道。\n"
                "-3-高性能卡拉OK模式，单独分离人声。htdemics\n"
                "-4-高性能专业音频模式，分离4个轨道。\n"
                "->")


while True:
    FunctionInput()
    if inp == "1":
        Function1()
    elif inp == "2":
        Function2()
    elif inp == "3":
        Function3()
    elif inp == "4":
        Function4()
    else:
        input("输入结果错误。")
