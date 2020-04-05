import time
needhelp = None
while needhelp not in ['需要', '不需要']:
    needhelp = input('小精灵：您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
    if needhelp == '需要':
        anyhelp = None
        while anyhelp not in ['1', '2', '3']:
            anyhelp = input('小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
            if anyhelp == '1':
                print('小精灵：推荐您去存取款窗！')
            elif anyhelp == '2':
               print('小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币') 
               exchange = input('小精灵：请问您需要兑换多少金加隆呢？')
               print('小精灵：好的，我知道了，您需要兑换'+exchange+'金加隆。')
               time.sleep(2)
               print('小精灵：那么，您需要付给我'+str(int(exchange)*51.3)+'人民币。')
            elif anyhelp == '3':
                print('小精灵：推荐您去咨询窗口！')
            else:
                print('小精灵：对不起，您的输入有误，请重新输入！')
    elif needhelp == '不需要':
        print('小精灵：好的，再见。')
    else:
        print('小精灵：对不起，您的输入有误，请重新确认！')
time.sleep(3)
print("交易结束！")