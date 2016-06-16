import datetime

class BankAccount(object):
    def __init__(self, acc_nr, owner, inital_balance):
        self.acc_nr = acc_nr
        self.owner = owner
        self.inital_balance = inital_balance
        self.transactions = []

    def add_transaction(self, date, amount):
        # create new transaction
        new_transaction = {'date': date, 'amount': amount}
        self.transactions.append(new_transaction)

    def add_transaction_interactive(self):
        new_transaction_amout = float(raw_input('Neue Transaktion:'))
        new_transaction_date = datetime.date.today().isoformat()
        new_transaction = {'date': new_transaction_date, 'amount': new_transaction_amout}
        self.transactions.append(new_transaction)
        

my_account = BankAccount('1045433', 'Marko Knoebl', 10)

print my_account.transactions

my_account.add_transaction('2016-04-30', -5)
my_account.add_transaction('2016-02-10', 10)
my_account.add_transaction_interactive()

print my_account.transactions
