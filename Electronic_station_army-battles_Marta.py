# Electronic station https://py.checkio.org/en/mission/army-battles/

# moderate
# marta

# Army battels
# Marta Vohnoutova

'''

Moderate
English RU
...Sir Ronald’s opponent - Umbert, has proved to be a very skillful warrior.
In addition, he was a good fifteen years younger, which gave him a
certain advantage. But Sir Ronald was also very strong -
he had the experience of participation in many battles and
in several major wars behind his back. And besides that,
in his youth he was known as the best duelist in this land.
Realizing that the forces are equal, each of them had followed the only
course possible - to call for help. Umbert sent for the reinforcement
his coachman on a horse, and Sir Ronald used a family horn that sounded
more than once in hot battles. The knight's castle was close enough for
the call to arms was heard back there. Nobody quite knew where the Umbert's
accomplices were located, and this made it difficult to come up with a strategy for the battle ahead.
Fortunately, the reinforcements for both sides arrived almost simultaneously.
Now it was more than a question of the girl's honor. There was no
peaceful solutions to this matter. One of the two armies must be destroyed.

In the previous mission - Warriors - you've learned how to make a duel
between 2 warriors happen. Great job! But let's move to something that
feels a little more epic - the armies! In this mission your task is to
add new classes and functions to the existing ones. The new class should
be the Army and have the method add_units() - for adding the chosen amount
of units to the army. The first unit added will be the first to go to fight,
the second will be the second, ...
Also you need to create a Battle() class with a fight() function,
which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army
and the first warrior of the second army. As soon as one of them dies -
the next warrior from the army that lost the fighter enters the duel,
and the surviving warrior continues to fight with his current health.
This continues until all the soldiers of one of the armies die.
In this case, the battle() function should return True, if the
first army won, or False, if the second one was stronger.

Note that army 1 have the advantage to start every fight!

example

Example:

chuck = Warrior()

bruce = Warrior()

carl = Knight()

dave = Warrior()

mark = Warrior()


fight(chuck, bruce) == True

fight(dave, carl) == False

chuck.is_alive == True

bruce.is_alive == False

carl.is_alive == True

dave.is_alive == False

fight(carl, mark) == False

carl.is_alive == False


my_army = Army()

my_army.add_units(Knight, 3)


enemy_army = Army()

enemy_army.add_units(Warrior, 3)


army_3 = Army()

army_3.add_units(Warrior, 20)

army_3.add_units(Knight, 5)


army_4 = Army()

army_4.add_units(Warrior, 30)


battle = Battle()


battle.fight(my_army, enemy_army) == True

battle.fight(army_3, army_4) == False



Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For computer games development.

Precondition:

    2 types of units
    For all battles, each army is obviously not empty at the beginning.

'''


class Warrior(object):
   def __init__(self,health=50):
      self.health = health    
      self.attack = 5
      self.is_alive = True
        

class Knight(Warrior):

    def __init__(self):
        super().__init__()        
        self.attack = 7
        self.axe = 66
        
class Army(object):
   def __init__(self):
      self.soldiers = []
      

   def add_units(self,soldier,sum_of_soldiers):
      self.soldier=soldier
      for x in range(sum_of_soldiers): 
         if soldier in [Warrior,Knight]:
            self.soldiers.append(soldier())
        
      return self.soldiers

class Battle(object):
   def __init__(self):
      pass
   
   def fight(self, army1,army2):
      beatten=False
      if type(army1) == Army and type(army2) == Army:
         i=0
         while len(army1.soldiers) > 0 and len(army2.soldiers) > 0:
            
            fight(army1.soldiers[0],army2.soldiers[0])
            
            if army1.soldiers[0].health <= 0:
               army1.soldiers.remove(army1.soldiers[0])
            if army2.soldiers[0].health <= 0:
               army2.soldiers.remove(army2.soldiers[0])

      if len(army2.soldiers) == 0:
         beatten = True
               
      elif len(army1.soldiers) == 0:
         beatten = False
         print('1',len(army1.soldiers),' 2',len(army2.soldiers))
      
      return beatten

def fight(fighter1,fighter2):
   while fighter1.is_alive and fighter2.is_alive:
      fighter2.health -= fighter1.attack        
      fighter2.is_alive = (fighter2.health > 0)        
      if fighter2.is_alive:
         fighter1.health -= fighter2.attack
         fighter1.is_alive = (fighter1.health > 0)
    
   return fighter1.is_alive  
#


chuck = Warrior()

bruce = Warrior()

carl = Knight()

dave = Warrior()

mark = Warrior()


assert fight(chuck, bruce) == True

assert fight(dave, carl) == False

assert chuck.is_alive == True

assert bruce.is_alive == False

assert carl.is_alive == True

assert dave.is_alive == False

assert fight(carl, mark) == False

assert carl.is_alive == False



my_army = Army()

my_army.add_units(Knight, 3)

enemy_army = Army()

enemy_army.add_units(Warrior, 3)


army_3 = Army()

army_3.add_units(Warrior, 20)

army_3.add_units(Knight, 5)


army_4 = Army()

army_4.add_units(Warrior, 30)


battle = Battle()


assert battle.fight(my_army, enemy_army) == True

assert battle.fight(army_3, army_4) == False

#
army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
print(battle.fight(army_1, army_2))
      
   

