class Accounts():
    def __init__(self,account,number,balance):
        self.__account=account
        self.__number=number
        self.__balance=balance


    def get_account(self):
        return self.__account


    def get_number(self):
        return self.__number


    def get_balance(self):
        return self.__balance


    def set_account(self,account):
        self.__account=account


    def set_number(self,number):
        self.__number=number


    def set_balance(self,balance):
        self.__balance=balance


class Payment():
    def __init__(self,account,charges,due,past,payable):
        self.__account=account
        self.__charges=charges
        self.__due=due
        self.__past=past
        self.__payable=payable



    def get_account(self):
        return self.__account



class fixedDepositacc(Accounts):
    def __init__(self,account,number,balance,rate,date,status):
        Accounts.__init__(self,account,number,balance)
        self.__rate=rate
        self.__date=date
        self.__status=status



    def get_rate(self):
        return self.__rate


    def set_rate(self,rate):
        self.__rate=rate


    def get_amount(self):
        return self.__amount



    def set_amount(self,amount):
        self.__amount=amount


    def get_date(self):
        return self.__date


    def set_date(self,date):
        self.__date=date


    def get_status(self):
        return self.__status


    def set_status(self,status):
        self.__status=status

    def computeInt(self):
        return self.__rate*self.get_balance()






