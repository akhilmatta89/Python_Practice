class Dog:
    species = "Canis familiaris"  # class attributes which is same for the entire class

    def __init__(self, breed, age):
        self.breed = breed  # Instance attributes which is diff for different instances
        self.age = age

    def bark(self):
        print(f"Woof! my breed is {self.breed} and my age was {self.age} and i belong to {self.species}", )


dog_1 = Dog("lab", 16)
dog_1.bark()

dog_2 = Dog(age=14, breed="german shepherd")
dog_2.bark()
