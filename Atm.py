class Atm:
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = 20000
    
    def cashWithdrawl(self,amount):
        self.balance = self.balance-amount
        print('balance in your account',self.balance)

    def balanceEnquiry(self):
        print('balance in your account',self.balance)

def main():
    cardNumber = input('enter your card number')
    pinnumber = input('enter your pin number')
    newUser = Atm(cardNumber,pinnumber)
    activity = int(input('press 1 for cash withdrawl,press 2 for balance enquiry'))
    if activity == 1:
        amount = int(input('enter the amount you want to withdraw'))
        newUser.cashWithdrawl(amount)
    elif activity == 2:
        newUser.balanceEnquiry()

main()