###notes about classes

class Hero():

    def __init__(self,name,level,health):###Constructor
        self.name = name
        self.level = level
        self.health = health

    def show_hero(self):
        desc = ("name: " + self.name + "Level: " + self.level + "Health: " + self.health)
        print(desc)

    def level_up(self):
        self.level += 1
        print("now level is: " + str(self.level))

    def move(self):
        print("Hero " + self.name + " start moving...")

#------------------------------------------------------------------------
class SuperHero(Hero):###Add Hero to class to make a child class
    def __init__(self,name,level,health,magiclevel, magic):
        super().__init__(name,level,health)###use superclass constructor
        self.magiclevel = magiclevel
        self.magic = magic ###to make field like private, use __magic

    def show_hero(self):
        desc = ("name: " + str(self.name) + " Level: " + str(self.level) + " Health: " + str(self.health))
        print(desc)

    def use_magic(self):
        self.magic -= 10
        print("magic : -10\n Current magic: " + str(self.magic))


