# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Animals:
    species = ''
    name = ''
    voice = ''
    state = ''
    weight = 0

    def __init__(self, weight, name, voice='Vote for EDPO!', state='exists'):
        # self.species = species
        self.name = name
        #self.voice = voice
        #self.state = state
        self.weight = weight

    def feed(self, food):
        self.state = 'fed'
        print(f'A {self.species} called {self.name} has consumed {food} and is now {self.state}!')

    def vocalise(self, call):
        self.state = 'talking'
        print(f'A {self.species} called {self.name} has heard {call}, said {self.voice} and is now {self.state}!')


class Goose(Animals):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.species = 'goose'
        self.voice = '`Honk!`'

    def lay_eggs(self, nmb_eggs):
        self.state = 'an apparatus for reproduction of egg'
        print(f'A {self.species} called {self.name} has laid {nmb_eggs} eggs and is now {self.state}!')


class Duck(Animals):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.species = 'duck'
        self.voice = '`Quack!`'

    def lay_eggs(self, nmb_eggs):
        self.state = 'an apparatus for reproduction of egg'
        print(f'A {self.species} called {self.name} has laid {nmb_eggs} eggs and is now {self.state}!')


class Chicken(Animals):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.species = 'chicken'
        self.voice = '`Cluck!`'

    def lay_eggs(self, nmb_eggs):
        self.state = 'an apparatus for reproduction of egg'
        print(f'A {self.species} called {self.name} has laid {nmb_eggs} eggs and is now {self.state}!')


class Cow(Animals):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.species = 'cow'
        self.voice = '`Moo!`'

    def milk(self, litres_to_milk):
        self.state = 'milked'
        print(f'A {self.species} called {self.name} has produced {litres_to_milk}l of milk and is now {self.state}!')

class Goat(Animals):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.species = 'goat'
        self.voice = '`Baa!`'

    def milk(self, litres_to_milk):
        self.state = 'milked'
        print(f'A {self.species} called {self.name} has produced {litres_to_milk}l of milk and is now {self.state}!')

class Sheep(Animals):
    def __init__(self, weight, name):
        super().__init__(weight, name)
        self.species = 'sheep'
        self.voice = '`Maa!`'

    def shear(self, wool_to_shear):
        self.state = 'shorn'
        print(f'A {self.species} called {self.name} has produced {wool_to_shear} cubic units of wool and is now {self.state}!')

def calculate_total_mass(animals):
    total_mass = 0
    for specimen in animals:
        if isinstance(specimen, Animals):
            added_mass = specimen.weight
            total_mass += added_mass
    return total_mass

def find_teh_heaviest(animals):
    max_mass = 0
    victim_name = ''
    victim_species = ''
    for specimen in animals:
        if (specimen.weight >= max_mass) and (isinstance(specimen, Animals)):
            max_mass = specimen.weight
            victim_name = specimen.name
    print(f'The fattest one is {victim_name} the {victim_species} with mass of {max_mass}, and that`s who shall be eaten first!')

goose_smokey = Goose(3, 'Smokey')
goose_mr_white = Goose(5.4, 'Mr. White')
cow_mary = Cow(300, 'Mary')
sheep_ramsteen = Sheep(42, 'Ramsteen')
sheep_curly = Sheep(39.9, 'Curly')
chicken_clucky = Chicken(2.7, 'Clucky')
chicken_cocky = Chicken(3.4, 'Cocky')
goat_vector = Goat(45, 'Vector')
goat_acme = Goat(56, 'Acme')
duck_darkwing = Duck(3.14, 'Darkwing')
animal = Animals(5928, 'Непродажный Обзорщик')

call = 'Ты кто такой, сука, чтоб это делать?!'
animal_farm = [goose_smokey, goose_mr_white, chicken_clucky, chicken_cocky, cow_mary, goat_vector, goat_acme, duck_darkwing]

print(goat_acme.vocalise(call))
print(cow_mary.vocalise(call))
print(sheep_ramsteen.vocalise(call))
print(chicken_cocky.vocalise(call))
print(goose_mr_white.vocalise(call))
print(duck_darkwing.vocalise(call))
print(duck_darkwing.lay_eggs(45))
print(sheep_curly.shear(90))
print(cow_mary.milk(10))
print(sheep_ramsteen.__dict__)
print(animal.__dict__)

print(calculate_total_mass(animal_farm))
print(find_teh_heaviest(animal_farm))


