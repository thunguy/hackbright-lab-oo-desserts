"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    """cache stores all cupcake instances by name"""
    cache = {}
    
    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        self.cache[name] = self

    def __repr__(self):
        """Human-readable printout for debugging."""
        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def add_stock(self, amount):
        """Add amount to self.qty"""
        self.qty += amount

    def sell(self, amount):
        """Sell the given amount of cupcakes and update self.qty."""
        
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
            return

        if self.qty < amount:
            self.qty = 0
            return

        self.qty -= amount

    @staticmethod
    def scale_recipe(ingredients, amount): 
        """Scale the list of ingredients by the given amount of cupcakes."""
        return [(ingredient, qty * amount) for ingredient, qty in ingredients]

    @classmethod
    def get(cls, name):
        """Return a cupcake from cls.cache if name exists"""
        if name not in cls.cache:
            return print("Sorry, that cupcake doesn't exist")
            
        
        return cls.cache[name]
        

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
