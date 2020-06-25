class AbstractCook:
    def __init__(self, Food = None, Drink = None):
        self.Food = Food
        self.Drink = Drink
        self.Food_massive = []
        self.Drink_massive = []

    def add_food(self, food_amount, food_price):
        self.Food_massive.append([food_amount, food_price])
    
    def add_drink(self, drink_amount, drink_price):
        self.Drink_massive.append([drink_amount, drink_price])

    def total(self):
        food_total = 0
        drink_total = 0
        for i in range(0, len(self.Food_massive)):
            food_total += self.Food_massive[i][0] * self.Food_massive[i][1]
        for i in range(0, len(self.Drink_massive)):
            drink_total += self.Drink_massive[i][0] * self.Drink_massive[i][1]
        total = food_total + drink_total
        total_string = "{}: {}, {}: {}, Total: {}".format(self.Food, food_total, self.Drink, drink_total, total)
        return total_string

class JapaneseCook(AbstractCook):
    def __init__(self):
        super().__init__(Food = 'Sushi', Drink = 'Tea')
        
class RussianCook(AbstractCook):
    def __init__(self):
        super().__init__(Food = 'Dumplings', Drink = 'Compote')

class ItalianCook(AbstractCook):
    def __init__(self):
        super().__init__(Food = 'Pizza', Drink = 'Juice')

if __name__ == '__main__':
    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")

