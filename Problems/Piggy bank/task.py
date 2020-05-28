class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.deposit_dollars = None
        self.deposit_cents = None

    def add_money(self, add_dollars, add_cents):
        self.deposit_dollars = add_dollars
        self.deposit_cents = add_cents
        self.dollars += self.deposit_dollars
        if self.cents + self.deposit_cents > 99:
            self.convert_cents()
        else:
            self.cents += self.deposit_cents

    def convert_cents(self):
        self.dollars += (self.cents + self.deposit_cents) // 100
        self.cents = (self.cents + self.deposit_cents) % 100