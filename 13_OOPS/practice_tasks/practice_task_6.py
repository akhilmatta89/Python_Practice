"""
Practice Task 7: Multiple Inheritance
Create two classes:

Artist with method paint() that prints "Painting a masterpiece"

Musician with method play_music() that prints "Playing guitar"

Create a class MultiTalentedPerson that inherits from both Artist and Musician and has its own method introduce() that prints "I am multi-talented!".

Create an object of MultiTalentedPerson and call all three methods.

"""

class Artist:
    def paint(self):
        print("Painting a masterpiece")

class Musician:
    def play_music(self):
        print("Playing guitar")

class MultiTalentedPerson(Artist, Musician):

    def introduce(self):
        print("I am multi-talented!")

m = MultiTalentedPerson()
m.introduce()
m.paint()
m.play_music()