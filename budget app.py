
class Category:
    def __init__(self, category):
        self.category=category
        self.ledger=[]
        self.total_amount=0
        self.withdrawal_amounts=[]

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def calculate_amounts(self):
        self.total_amount=0
        for dep in self.ledger:
            self.total_amount+=dep['amount']

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.withdrawal_amounts.append(amount)
            return True
        else:
            return False

    def withdrawal_amount(self):
        total_withdrawal=sum(self.withdrawal_amounts)
        return total_withdrawal


    def get_balance(self):
        self.calculate_amounts()
        return self.total_amount

    def transfer(self, amount, Category):

        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': f'Transfer to {Category.category}'})
            Category.deposit(amount, f'Transfer from {self.category}')
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
        spending="\n".join([(dep['description'][:23] + f"{(round(float(dep['amount']), 2)):.2f}".rjust(30-len(dep['description'][:23]))) for dep in self.ledger])
        self.calculate_amounts()
        total='\n' + 'Total: '+ str(round(self.total_amount, 2))
        return title + spending + total
    def name(self):
        return self.category



def create_spend_chart(categories):
    withdrawal_amounts_list=[]
    for category in categories:
        withdrawal_amounts_list.append(category.withdrawal_amount())
    total_cost=sum(withdrawal_amounts_list)
    percentage_list=[]
    for withdrawal in  withdrawal_amounts_list:
        percentage_list.append(((withdrawal/total_cost)*100)//10*10)
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):  # From 100% to 0%
        row = f"{str(i).rjust(3)}|"
        for percentage in percentage_list:
            row += " o " if percentage >= i else "   "
        chart += row + " \n"

        # Add the separator line
    chart += "    " + "-" * (len(categories) * 3 + 1)

    # Prepare the category names vertically
    max_length = max(len(category.name()) for category in categories)
    for i in range(max_length):
        row = "     "
        for category in categories:
            row += (category.name()[i] + "  ") if i < len(category.name()) else "   "
        chart +='\n' + row

    return chart


food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(10, "formal clothes")
auto=Category('Auto')
food.transfer(500, auto)
auto.withdraw(300, 'fixing car')
barber=Category('barber')
food.transfer(100, barber)
barber.withdraw(80, "nice haircut")
categories=[food, clothing, auto, barber]
print(create_spend_chart(categories))
