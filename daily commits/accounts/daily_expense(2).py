#function defining initially
def __init__(self):
        self.income = 0
        self.expenses = 0
        self.expense_list = []
        self.expense_name = []
        self.income_name = []
        self.income_list = []
 #income adding       

def income_sum(self):
        self.income = sum(self.income_list)
def expense_ask(self):
        add_expense = input('Add expense? [y/n]: ')
        return add_expense
def expense_sum(self):
        self.expenses = sum(self.expense_list)
def income_check(self):
        if not self.income_list:
            print('Please enter atleast one source of income. ')
            self.prompt_income()
        else:
            return
def prompt_income(self):
        x = False
        while not x:
            result = self.income_ask()
            if result == 'y':
                income_input = int(input('Enter source of income.[Numbers Only]: '))
                self.income_list.append(income_input)
                income_name = input('Enter income name. [Name Only]: ')
                self.income_name.append(income_name)
            else:
                self.income_check()