from random import randint
import statistics
import matplotlib.pyplot as plt

buyers = []
sellers = []

"""
class Day:
    def __init__(self, sellers: list = None, buyers: list = None):
        if sellers is None:
            self.sellers = []
        if buyers is None:
            self.buyers = []
"""


class Entity:
    def __init__(self):
        pass


class Seller(Entity):
    def __init__(self, cost: int):
        super().__init__()
        self.cost = cost
        self.price = cost * 1.5  # initial price is at 50% markup
        self.sold_item = False
        self.offers = []

    def set_price(self,):
        if not self.sold_item:
            if self.price > self.cost:
                self.price -= 1  # decrease price by 1 if item couldn't be sold
        else:
            self.price += 1  # increase price by 1 if item could be sold

    def sell_item(self):
        if self.offers is not None and not self.sold_item:
            highest = self.get_highest_offer()
            if highest is not None:
                if highest.optimum >= self.price:
                    highest.bought_item = True
                    print(hex(id(highest)))
                    print(f"seller {hex(id(self))} sold item for {self.price} to highest bidder ({highest.optimum}) ({hex(id(highest))})")
                    self.sold_item = True
        self.offers = []

    def get_highest_offer(self):
        if len(self.offers) > 0:
            highest = self.offers[0]
            for o in self.offers:
                if o.optimum > highest.optimum:
                    highest = o
            return highest


class Buyer(Entity):
    def __init__(self, budget: int):
        super().__init__()
        self.budget = budget
        self.maximum = None
        self.optimum = 0  # initial optimum is for free (0 CHF)
        self.bought_item = False

    def set_optimum(self):
        if not self.bought_item:
            if self.optimum < self.budget:
                self.optimum += 1  # raise optimum by 1 if no item could be bought
        else:
            self.optimum -= 1  # decrease optimum by 1 if item could be bought

    def make_offer(self):
        if not self.bought_item:
            get_cheapest_seller().offers.append(self)
            print(f"Buyer offered cheapest seller ({get_cheapest_seller().price}) {self.optimum}")


def get_cheapest_seller():
    cheapest = sellers[0]
    for s in sellers:
        if s.price < cheapest.price and not s.sold_item:
            cheapest = s
    return cheapest


if __name__ == '__main__':

    for i in range(20):
        sellers.append(Seller(cost=50 + randint(-10, 10)))  # cost varies +- 10

    for i in range(40):
        buyers.append(Buyer(budget=50 + randint(-10, 10)))  # budget varies +- 10

    average_prices = []
    average_offers = []

    for i in range(200):
        print(f"**** Day {i} ****")
        buyer_offers = []
        seller_prices = []

        for buyer in buyers:
            buyer.bought_item = False
            buyer.make_offer()

        for seller in sellers:
            seller.sold_item = False
            seller.sell_item()

        for buyer in buyers:
            buyer.set_optimum()
            buyer_offers.append(buyer.optimum)

        for seller in sellers:
            seller.set_price()
            seller_prices.append(seller.price)

        average_prices.append(statistics.mean(seller_prices))
        average_offers.append(statistics.mean(buyer_offers))

    plt.plot(average_prices)
    plt.plot(average_offers)
    plt.show()





