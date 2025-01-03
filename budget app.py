
class Category:
    def __init__(self, category):
        self.category=category
        self.ledger=[]
        self.total_amount=0

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def calculate_amounts(self):
        self.total_amount=0
        for dep in self.ledger:
            self.total_amount+=dep['amount']

    def withdraw(self, amount, description=''):
        self.calculate_amounts()
        if self.total_amount > amount:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False


    def get_balance(self):
        self.calculate_amounts()
        return self.total_amount





def create_spend_chart(categories):
    pass

food=Category('food')
food.deposit(9000,'groceries')
food.deposit(2000, 'alcohol')
food.withdraw(10000, 'more groceries')
food.deposit(4000, 'more alcohol')

print(food.get_balance())
