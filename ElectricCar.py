from car import Car
class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year, dianliang):
        super().__init__(make, model, year)
        self.dianliang = dianliang

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model + ' ' + str(self.dianliang)
        return long_name.title()


# my_tesla = Car('tesla', 'model s', 2016)
my_tesla = ElectricCar('tesla', 'model s', 2016, 3000)

print(my_tesla.get_descriptive_name())