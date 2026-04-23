import json

class FinanceEngine:
    def __init__(self):
        self.balance = 0.0
        self.expenses = []

    def add_record(self, amount, category, t_type="expense"):
        if t_type == "income":
            self.balance += amount
        else:
            self.balance -= amount
            self.expenses.append({"amount": amount, "category": category})

    def get_budget_status(self):
        """Logic to determine financial health."""
        if self.balance < 0:
            return "Critical: Overbudget"
        elif self.balance < 500:
            return "Warning: Low Reserves"
        return "Healthy"

    def calculate_interest(self, rate, years):
        """Demonstrating formula implementation: A = P(1 + rt)"""
        return self.balance * (1 + (rate/100) * years)