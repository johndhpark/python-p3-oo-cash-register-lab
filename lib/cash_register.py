#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.lastItem = None
    self.items = []

  def add_item(self, name, price, quantity = 1):
    self.total += (price * quantity)
    self.lastItem = { "name": name, "price": price, "quantity": quantity }

    for _ in range(quantity):
      self.items.append(name)

  def apply_discount(self):

    if self.discount != 0:
      self.total = float(self.total * ((100 - self.discount) / 100))
      print(f"After the discount, the total comes to ${round(self.total)}.")
      return

    print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.lastItem != None:
      self.total -= (self.lastItem["price"] * self.lastItem["quantity"])


