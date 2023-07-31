# -*- coding: gbk -*-
import os


def WinUpLoc(loc):  # ��Windows��ʽ�����ļ����ڵ�ԭ��Ŀ¼
    if loc[0] == '''"''':  # ȥ��˫���š����һ����б��
        loc = loc[1:-1]
    lis = loc.replace("\\", "/").split('/')
    lis.pop()
    loc = ''
    for ji in range(len(lis)):
        loc = loc + str(lis[ji]) + '/'
    return loc[0:-1].replace("/", "\\")


def Function1():
    fileAdrStr = input("��Demucs������Ƶ��ָ������OKģʽ��\n�����ļ���ַ�����Ͻ�CMD��\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("������ת��CMDִ�С�\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n mdx_extra --two-stems=vocals'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\nִ����ϡ�")


def Function2():
    fileAdrStr = input("��Demucs������Ƶ��ָ��רҵ��Ƶģʽ��\n�����ļ���ַ�����Ͻ�CMD��\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("������ת��CMDִ�С�\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n mdx_extra'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\nִ����ϡ�")


def Function4():
    fileAdrStr = input("��Demucs������Ƶ��ָ��������רҵ��Ƶģʽ��\n�����ļ���ַ�����Ͻ�CMD��\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("������ת��CMDִ�С�\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n htdemucs'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\nִ����ϡ�")


def Function3():
    fileAdrStr = input("��Demucs������Ƶ��ָ��������רҵ��Ƶģʽ��\n�����ļ���ַ�����Ͻ�CMD��\n")
    if fileAdrStr[0] != '''"''':
        fileAdrStr = '''"''' + fileAdrStr + '''"'''
    adrStr = WinUpLoc(fileAdrStr)
    print("������ת��CMDִ�С�\n-------------------------------")
    os.system("pip show demucs")
    cmd = r'''demucs {} -o "{}" -n htdemucs --two-stems=vocals'''.format(fileAdrStr, adrStr)
    os.system(cmd)
    print(cmd)
    input("-------------------------------\nִ����ϡ�")


def FunctionInput():
    global inp
    inp = input("-ѡ�����ģʽ��\n"
                "-1-����OKģʽ����������������mdx_extra\n"
                "-2-רҵ��Ƶģʽ������4�������\n"
                "-3-�����ܿ���OKģʽ����������������htdemics\n"
                "-4-������רҵ��Ƶģʽ������4�������\n"
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
        input("����������")
