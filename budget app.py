
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
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False


    def get_balance(self):
        self.calculate_amounts()
        return self.total_amount

    def transfer(self, amount, Category):

        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {Category.category}'})
            Category.deposit(amount, f'transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        self.calculate_amounts()
        if self.total_amount < amount:
            return False
        else:
            return True

    def __str__(self):
        title=f'{self.category:*^30}' + '\n'
        spending="\n".join([(dep['description'][:23] + f'{(round(float(dep['amount']), 2)):.2f}'.rjust(30-len(dep['description'][:23]))) for dep in self.ledger])
        self.calculate_amounts()
        total='\n' + 'Total: '+ str(self.total_amount)
        return title + spending + total



def create_spend_chart(categories):
    pass


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
