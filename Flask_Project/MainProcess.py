from accounts import Accounts
from accounts import Payment
from accounts import fixedDepositacc



def processAccounts():
    accountsList = []
    accountsFile = open('static/file/acc', 'r')
    for alist in accountsFile:
        list = alist.split(',')
        s = Accounts(list[0], list[1], int(list[2]))

        accountsList.append(s)

    return accountsList



def processFixedDeposit():
    fixedDepositList=[]
    accountsFile = open('static/file/fixedDeposit', 'r')

    for i in accountsFile:
        list=i.split(',')
        a=fixedDepositacc(list[0],list[1],float(list[2]),float(list[3]),list[4],list[5])

        fixedDepositList.append(a)

    return fixedDepositList

#def calculateInterest():
 #   file = open('static/file/fixedDeposit', 'r')
  #  for i in file:
   #     list = i.split(',')
    #    interest = 0



def calculateBalance():
    accountsFile = open('static/file/acc', 'r')
    for alist in accountsFile:

        list = alist.split(',')
        total=0
        total=total+float(list[2])

    return total



def processPayment():
    paymentList=[]
    paymentFile=open('static/file/payment','r')
    for list in paymentFile:
        list1=list.split(',')
        s=Payment(list1[0],list1[1],list1[2],list1[3],list[4])

        paymentList.append(s)

    return paymentList


