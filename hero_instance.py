from classes import *

skeletonHero = Hero("Daniel", 10, 100)
skeletonHero.level_up()
skeletonHero.move()
skeletonHero.level_up()

nastyaHero = SuperHero("Nastya",20, 100,5,200)
nastyaHero.move()
nastyaHero.show_hero()
nastyaHero.use_magic()
nastyaHero.magic = 12
nastyaHero.use_magic()