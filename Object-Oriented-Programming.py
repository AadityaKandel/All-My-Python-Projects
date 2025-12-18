'''
This is my first take in Object Oriented Programming. My explanation is something like this.
I have created a Character class which contains several methods. Among these methods, the
__init__ method is the first method that runs automatically and initializes all the variables
that are given. Not just that, it takes several arguments that define a character.

With that, I have created other methods that are responsible for checking health of a character,
taking damage, and healing. With the class at hand, I created three players. These players are 
known as objects who share the same 'Character' class.

--------------------------------
IMPORTANT THING TO REALISE HERE-
--------------------------------
Since class is a blueprint to everything, it shares the same variable to everyone.
No matter it is the enemy or player or you, all of you share the same value.
If you use any memory modifying applications like Cheat Engine to find your health
variable, you can change it. However, if you create a specific .dll or .asm injection
to hack the memory, you will end up hacking the variable of the entire class. 
Not just you but all players will have unlimited health. To avoid this, you need to
find common things about these players and exclude yourself.
'''

class Character:

    def __init__(self,name,max_health,no_of_guns,max_armor,gunID,dmg):
        self.name=name
        self.health = max_health
        self.gun_numbers = no_of_guns
        self.armor = max_armor
        self.currentGunID = gunID
        self.dmgPerShot=dmg
    
    def check_healthStatus(self):
        if self.health<=0:
            print(f"{self.name} has been dead")
        else:
            print(f"{self.name} is alive")
            print(f"Health Remaining: {self.health}")

        return self.health
    
    def take_damage(self):
        self.health-=self.dmgPerShot
        return self.health

    def heal(self):
        if self.health<=0:
            print(f"Cannot Heal Because {self.name} is already dead")
            return

        self.health+=20.0

player1 = Character("Aaditya",100.0,49,100.0,9,5.0)
player2 = Character("Bot1",200.0,29,200.0,8,10.0)
player3 = Character("Bot2",400.0,19,400.0,7,20.0)

player1.take_damage()
player2.take_damage()
player3.take_damage()

player1.check_healthStatus()
player2.check_healthStatus()
player3.check_healthStatus()

while(player2.take_damage()!=0):
    player2.take_damage()

player2.check_healthStatus()
player2.heal()
