from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Meat, Vegetable, Fruit, Seed



#foods
veg = Vegetable(1)
meat = Meat(4)
fruit = Fruit(5)
seeds = Seed(5)

owl = Owl("Pip", 10, 10)
print(owl)
print(owl.make_sound())
owl.feed(meat)
print(owl.feed(veg))
print(owl)

hen = Hen("Harry", 10, 10)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

mice = Mouse('Jerry', 5, 'USA')
print(mice)
print(mice.make_sound())
mice.feed(veg)
mice.feed(fruit)
print(mice.feed(meat))
print(mice.feed(seeds))
print(mice.living_region)

dog = Dog('Spike', 15, 'USA')
print(dog)
print(dog.make_sound())
dog.feed(meat)
print(dog.feed(veg))
print(dog.feed(fruit))
print(dog.feed(seeds))
print(dog.living_region)

cat = Cat('Tom', 3, 'USA')
print(cat)
print(cat.make_sound())
cat.feed(meat)
cat.feed(veg)
print(cat.feed(fruit))
print(cat.feed(seeds))
print(cat.living_region)

tigers = Tiger('Tiger', 10, 'USA')
print(tigers)
print(tigers.make_sound())
cat.feed(meat)
print(cat.feed(veg))
print(cat.feed(fruit))
print(cat.feed(seeds))
print(cat.living_region)


# first zero test
import unittest
from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Fruit, Meat, Seed

class WildFarmTests(unittest.TestCase):
    def test_first_zero(self):
        owl = Owl("Pip", 10, 10)
        self.assertEqual(str(owl), "Owl [Pip, 10, 10, 0]")
        meat = Meat(4)
        self.assertEqual(owl.make_sound(), "Hoot Hoot")
        owl.feed(meat)
        veg = Vegetable(1)
        owl.feed(veg)
        self.assertEqual(owl.feed(veg), "Owl does not eat Vegetable!")
        self.assertEqual(str(owl), "Owl [Pip, 10, 11.0, 4]")

if __name__ == "__main__":
    unittest.main()