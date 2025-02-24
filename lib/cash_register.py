#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.last_transaction = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        # Ensure the price is a numeric value (float or int)
        if not isinstance(price, (int, float)):
            raise ValueError("Price must be a numeric value.")

        # Add price * quantity to the total
        self.total += price * quantity
        self.last_transaction = price * quantity

        # Track the item with its title, price, and quantity
        self.items.extend([title] * quantity)  # Store only the title, repeated by quantity

    def apply_discount(self):
        if self.discount > 0:
            # Apply discount (assuming discount is a percentage)
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Print success message with updated total (formatted without decimals)
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

    def items_list(self):
        # Return the list of item titles, repeated according to their quantity
        return self.items
