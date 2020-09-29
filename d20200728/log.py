import time

def savelog(savedir, money, balance, mode):
    if mode:
        type = "출금"
    else:
        type = "입금"
    with open(savedir,'w',encoding='utf-8') as file:
        file.write(str(time.ctime())+"출금: "+str(money)+"잔액: "+str(balance)+'\n')