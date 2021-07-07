

class user:
    def __init__(self, first_name, last_name, amount):
        self.firstname = first_name
        self.lastname = last_name
        self.amount = amount

    def make_Deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"Your new balance is: {self.amount}" )

user1 = user('Samir','Hossain', 100000)
user2 = user('Jim','Carrey', 950000)
user3 = user('Mike','Stone', 5000)

user1.make_Deposit(50)
user1.make_Deposit(100)
user1.make_Deposit(5)
user1.make_withdrawal(10)
user1.display_user_balance()
print(user1.amount)

user2.make_Deposit(50)
user2.make_Deposit(10)
user2.make_withdrawal(10)
user2.make_withdrawal(5)
user2.display_user_balance()
print(user2.amount)

user3.make_Deposit(500)
user3.make_withdrawal(10)
user3.make_withdrawal(5)
user3.make_withdrawal(595)
user3.display_user_balance()
print(user3.amount)