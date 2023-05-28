class Expense:
    def __init__(self, name, category, amount):
        """
        Expense class constructor.

        Args:
        - name (str): The name of the expense.
        - category (str): The category of the expense.
        - amount (float): The amount spent on the expense.

        Initializes the instance variables with the provided values.
        """
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self) -> str:
        """
        String representation of the Expense object.

        Returns:
        - str: A formatted string representing the Expense object.

        Overrides the built-in __repr__ method to provide a customized string representation
        of the Expense object when printed or used in the interactive console.
        """
        return f"<Expense: {self.name}, {self.category}, {self.amount}>"

