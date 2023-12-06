class Zooshop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def find_most_expensive_breed(self):
        if not self.animals:
            return None

        most_expensive_breed = max(self.animals, key=lambda x: x.cost)
        return most_expensive_breed

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f"{animal.__class__.__name__}: {animal.breed}, Cost: {animal.cost}\n")


class Animal:
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    def move(self):
        raise NotImplementedError("Subclasses should implement this method")


class Fish(Animal):
    def move(self):
        return "Swimming"


class Bird(Animal):
    def move(self):
        return "Flying"


zooshop = Zooshop()

fish1 = Fish(breed="Goldfish", cost=10)
fish2 = Fish(breed="Clownfish", cost=15)
bird1 = Bird(breed="Parrot", cost=30)
bird2 = Bird(breed="Canary", cost=20)

zooshop.add_animal(fish1)
zooshop.add_animal(fish2)
zooshop.add_animal(bird1)
zooshop.add_animal(bird2)

most_expensive = zooshop.find_most_expensive_breed()
if most_expensive:
    print(f"The most expensive breed is {most_expensive.breed} with a cost of {most_expensive.cost}")
else:
    print("No animals in the zoo.")

zooshop.write_to_file("zooshop_info.txt")
