class animal:
    name="human"
    leg=2
    food="omnivorous"
    enviroment="anywhere, but don't in the Antarica"
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Legs: {self.leg}")
        print(f"Food: {self.food}")
        print(f"Environment: {self.enviroment}")
human=animal()
human.show_info()
lion=animal()
lion.name="lion"
lion.leg=4
lion.food="carnivorous"
lion.enviroment="savannah"
print("\n------------------------------------\n")
lion.show_info()
print("\n------------------------------------\n")
rabbit=animal()
rabbit.name="rabbit"
rabbit.leg=4
rabbit.food="herbivorous"
rabbit.enviroment="forest"
rabbit.show_info()