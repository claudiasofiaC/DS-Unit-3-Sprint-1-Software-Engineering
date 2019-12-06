"""
This is the file containing the class Acme
"""
from random import randint


class Product():
    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammibility=0.5,
        identifier=randint(1000000, 9999999)
    ):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammibility = flammibility
        self.identifier = identifier

    def stealability(self):
        val_stealish = self.price / self.weight
        if val_stealish < 0.5:
            return print('Not so stealable.')
        elif val_stealish >= 0.5 and val_stealish < 1.0:
            return print('Kinda stealable...')
        else:
            return print('Very Stealable!!')

    def explode(self):
        exp_factor = self.flammibility * self.weight
        if exp_factor < 10:
            return print('...fizzle')
        elif exp_factor >= 10 and exp_factor < 50:
            return print('...boom!')
        else:
            return print('..BABOOM!!!')


class BoxingGlove(Product):
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flamibility=0.5,
        identifier=randint(1000000, 9999999)
    ):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammibility = flamibility
        self.identifier = identifier

    def explode(self):
        return print("... It's a glove.")

    def punch(self):
        if self.weight < 5:
            return print('That tickles.')
        elif self.weight >= 5 and self.weight < 15:
            return print('Hey, that hurt!')
        else:
            return print("OUCH!!")

#prod = AcmeProduct('Toy', 20, 5, .2)
# print(prod.__dict__)

# autopep8 -i -a acme.py
