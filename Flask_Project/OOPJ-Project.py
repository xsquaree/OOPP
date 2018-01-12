from flask import Flask, render_template, request
from wtforms import Form, StringField, validators


import MainProcess


app = Flask(__name__)


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/accounts')
def accounts():
    return render_template('accounts.html')


@app.route('/home')
def home():
    userslist=[]
    userslist= MainProcess.processAccounts() #first
    totalBalance=MainProcess.calculateBalance()

    fdaList=[]
    fdaList=MainProcess.processFixedDeposit()
    return render_template('home.html', users=userslist, count=len(userslist),totalBalance=totalBalance, fda=fdaList)

@app.route('/fda')
def fda():
    return render_template('fixedDeposit.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')





if __name__ == '__main__':
    app.run()
