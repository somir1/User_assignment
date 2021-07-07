

class user:
    def __init__(self, first_name, last_name, amount):
        self.firstname = first_name
        self.lastname = last_name
        self.amount = amount

    def make_Deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"Your new balance is: {self.amount}" )


user1 = user('Samir','Hossain', 100000)
user2 = user('Jim','Carrey', 950000)
user3 = user('Mike','Stone', 5000)

user1.make_Deposit(50).make_Deposit(100).make_Deposit(5).make_withdrawal(10).display_user_balance()

user2.make_Deposit(50).make_Deposit(10).make_withdrawal(10).make_withdrawal(5).display_user_balance()

user3.make_Deposit(500).make_withdrawal(10).make_withdrawal(5).make_withdrawal(595).display_user_balance()