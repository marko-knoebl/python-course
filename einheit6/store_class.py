# Klasse: definiert eine Datenstruktur + Verhalten

class StoreItem(object):
    # Initialisierungsfunktion
    def __init__(self, name, price, weight, color):
        # self steht immer fuer das aktuelle Objekt
        #   (in diesem Fall ein StoreItem)
        # speichere Variablen ab
        self.name = name
        self.price = price
        self.weight = weight
        self.color = color

    def price_per_kg(self):
        return self.price / self.weight

    def netto_price(self):
        return self.price / 1.2

# ich Klassen wiederverwenden
# Die Klasse Beverage soll von StoreItem "erben"
class Beverage(StoreItem):
    def netto_price(self):
        return self.price / 1.1

# test:
bread = StoreItem('Brot', 1.99, 0.5, 'brown')
print bread
print bread.name
print bread.weight

print bread.price_per_kg()

print bread.price
print bread.netto_price()


wine = Beverage('Wein', 4.99, 0.75, 'red')

print wine.price_per_kg()
print wine.netto_price()
