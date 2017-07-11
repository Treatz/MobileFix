"""
GO!
Characters

Characters are (by default) Objects setup to be puppeted by Players.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter, TICKER_HANDLER

class Character(DefaultCharacter):
# [...]
    def at_object_creation(self):
        """
        Called only at initial creation. This is a rather silly
        example since ability scores should vary from Character to
        Character and is usually set during some character 
        generation step instead.
        """
        #set persistent attributes
        self.db.tradition = "None"
        self.db.essence = "None"
        self.db.concept = "None"
        self.db.strength = 0
        self.db.dexterity = 0
        self.db.stamina = 0
        self.db.manipulation = 0
        self.db.appearance = 0
        self.db.perception = 0
        self.db.intelligence = 0
        self.db.wits = 0
        self.db.conscious = 1
        self.db.alive = 1
        self.db.sight = 0
        self.db.conscious = 1
        self.db.alertness = 0
        self.db.athletics = 0
        self.db.awareness = 0
        self.db.brawl = 0
        self.db.intimidation = 0
        self.db.streetwise = 0
        self.db.drive = 0
        self.db.firearms = 0
        self.db.martialarts = 0
        self.db.melee = 0
        self.db.meditation = 0
        self.db.stealth = 0
        self.db.astrology = 0
        self.db.computer = 0
        self.db.language = 0
        self.db.medicine = 0
        self.db.occult = 0
        self.db.charisma = 9
        self.db.rituals = 0
        self.db.correspondence = 0
        self.db.entropy = 0
        self.db.forces = 0
        self.db.life = 0
        self.db.matter = 0
        self.db.mind = 0
        self.db.prime = 0
        self.db.spirit = 0
        self.db.time = 0
        self.db.quintessence = 0
        self.db.arete = 0
        self.db.willpower = 0
        self.db.arcane = 0
        self.db.belief = 0
        self.db.familiar = 0
        self.db.luck = 0
        self.db.resources = 0
        self.db.target = self
        self.db.attacker = self
        self.db.bashing = 0
        self.db.lethal = 0
        self.db.weapon = 0
        self.db.invis = 0
        self.db.blessed = 0
        self.db.cursed = 0
        self.db.burned = 0
        self.db.astro = 0
        self.db.starsign = 0
        self.db.attack_not = 1
        self.touch = 0
        self.intimidated = 0

        TICKER_HANDLER.add(60, self.heal)
        TICKER_HANDLER.add(120, self.heal_lethal)
        TICKER_HANDLER.add(180, self.spells)
        TICKE_HANDLER.add(15, self.ban)
        return

    def ban(self, *args, **kwards):
        if(self.db.ban  == self.location):
            self.msg("This area does not want you here!.")
            self.db.cursed = int(self.db.cursed) + 1
            self.db.finalban = int(self.db.finalban) + 1
        elif(self.db.finalban > 0):
            self.db.cursed = int(self.db.cursed) - 1
            self.db.finalban = int(self.db.finalban) - 1
            self.msg("You are beginning to feel better.,")
    def spells(self, *args, **kwards):
        if(self.db.rush > 0):
            if self.db.move_speed == "zoom":
                self.db.move_speed = "sprint"
            elif self.db.move_speed == "sprint":
                self.db.move_speed = "run"
            elif self.db.move_speed == "run":
                self.db.move_speed = "walk"
            elif self.db.move_speed == "walk":
                self.db.move_speed = "stroll"  
            self.db.rush = self.db.rush - 1

        if(self.db.push > 0):
            self.db.push = self.db.push - 1
            self.db.strength = self.db.strength - 1
            self.msg("You have lost some of your strength.")
        if(self.db.kinetic == 1):
            self.msg("Your kinetic boost is leaving you.")
            self.db.kinetic = 0 
        if(int(self.db.attack_not) == 0):
            self.db.attack_not = 1
        if(self.db.astro == 1):
            self.db.astro = 0
        if(self.db.burned > 0):
            self.msg("You recover some of your natural luck.")
            self.db.burned = self.db.burned - 1
        if(self.db.invis == 1):
            self.db.invis = 0
            self.msg("You have become visible.")
        if(self.db.move_speed == "freeze"):
            self.msg("Time begins to move normally again.")
        if(self.db.sight == 1):
            self.msg("Your vision to the spirit world fades.")
            self.db.sight = 0
        if self.db.blessed > 0:
           self.msg("Your luck is starting to fade.")
           self.db.blessed = int(self.db.blessed) - 1
        if self.db.blessed < 0:
           self.msg("The hex has begun to leave you.")
           self.db.blessed = int(self.db.blessed) + 1
        if(self.db.touch == 1):
            if self.db.alive:
                self.msg("You lose grasp on the spirit world.")
            else:
                self.msg("You lose graph on the physical world.")
            self.db.touch = 0
        if(self.db.alive == 0):
            self.db.conscious = 1
            self.msg("You take a deep breath of astral air.")


    def heal_lethal(self, *args, **kwargs):
        if(self.db.lethal > 0 and self.db.alive == 1):
            self.msg("You heal 1 point of lethal damage.")
            self.db.lethal = self.db.lethal  - 1


        if((self.db.lethal == 0 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: O O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: / O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: / / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: / / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: / / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: / / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: / / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: / / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 12)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 13)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 14)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 0
                self.db.alive = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X / / / / /  ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 12)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X X / / / /   ")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        
        
        if((self.db.lethal == 3 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0


        if((self.db.lethal == 4 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X X X / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        

        if((self.db.lethal == 5 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X X / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 0
                self.db.alive = 0                

        if((self.db.lethal == 6 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X X O")
                self.db.conscious = 1
                
        if((self.db.lethal == 6 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 6 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                

        if((self.db.lethal == 7 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 0
                self.db.alive = 0
        
                
    def heal(self, *args, **kwargs):
        if(self.db.bashing > 0 and self.db.alive == 1):
            self.msg("You heal 1 point of bashing damage.")
            self.db.bashing = self.db.bashing - 1

        if((self.db.lethal == 0 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: O O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: / O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: / / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: / / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: / / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: / / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: / / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: / / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 12)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 13)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 14)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X / / / / /  ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 12)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X X / / / /   ")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        
        
        if((self.db.lethal == 3 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0


        if((self.db.lethal == 4 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X X X / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        

        if((self.db.lethal == 5 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X X / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0                

        if((self.db.lethal == 6 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X X O")
                self.db.conscious = 1
                
        if((self.db.lethal == 6 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 6 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 0
                self.db.alive = 0
                

        if((self.db.lethal == 7 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        

    def get_abilities(self):
        """
        Simple access method to return ability 
        scores as a tuple (str,agi,mag)
        """
        return self.db.strength, self.db.agility, self.db.magic

    def is_alive(self):
        return self.db.alive

    def at_post_puppet(self):

        super(Character, self).at_post_puppet()

        if((self.db.lethal == 0 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: O O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: / O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: / / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: / / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: / / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: / / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: / / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: / / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 12)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 13)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 0 ) and ( self.db.bashing == 14)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X O O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X / / / / /  ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 1 ) and ( self.db.bashing == 12)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X / O O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X / / O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X / / / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X / / / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X / / / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X / / / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X X / / / /   ")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 9)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 10)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 2 ) and ( self.db.bashing == 11)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        
        
        if((self.db.lethal == 3 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X O O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X / O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X / / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X / / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 7)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 3 ) and ( self.db.bashing == 8)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0


        if((self.db.lethal == 4 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X O O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X / O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X / / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X X X / / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 5)):
                self.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.conscious = 0
                
        if((self.db.lethal == 4 ) and ( self.db.bashing == 6)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 0
                self.db.alive = 0
        

        if((self.db.lethal == 5 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X O O")
                self.db.conscious = 1
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X X / O")
                self.db.conscious = 1
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.conscious = 0
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 3)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 5 ) and ( self.db.bashing == 4)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0                

        if((self.db.lethal == 6 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X X O")
                self.db.conscious = 1
                
        if((self.db.lethal == 6 ) and ( self.db.bashing == 1)):
                self.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.conscious = 0
                
        if((self.db.lethal == 6 ) and ( self.db.bashing == 2)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
                

        if((self.db.lethal == 7 ) and ( self.db.bashing == 0)):
                self.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.conscious = 1
                self.db.alive = 0
        
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: O O O O O O O")
                self.db.target.db.conscious = 1
                

        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: / O O O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: / / O O O O O")
                self.db.target.db.conscious = 1
                        
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 3)):
                self.db.target.msg(prompt="|X|[wHealth: / / / O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 4)):
                self.db.target.msg(prompt="|X|[wHealth: / / / / O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 5)):
                self.db.target.msg(prompt="|X|[wHealth: / / / / / O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 6)):
                self.db.target.msg(prompt="|X|[wHealth: / / / / / / O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 7)):
                self.db.target.msg(prompt="|X|[wHealth: / / / / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 8)):
                self.db.target.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 9)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 10)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 11)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 12)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 13)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 0 ) and ( self.db.target.db.bashing == 14)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0
                
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X O O O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: X / O O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: X / / O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 3)):
                self.db.target.msg(prompt="|X|[wHealth: X / / / O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 4)):
                self.db.target.msg(prompt="|X|[wHealth: X / / / / O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 5)):
                self.db.target.msg(prompt="|X|[wHealth: X / / / / / O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 6)):
                self.db.target.msg(prompt="|X|[wHealth: X / / / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 7)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / / / /  ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 8)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 9)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 10)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 11)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 1 ) and ( self.db.target.db.bashing == 12)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X X O O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: X X / O O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 3)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / / O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 4)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / / / O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 5)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / / / / O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 6)):
                self.db.target.msg(prompt="|X|[wHealth: X X / / / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 7)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / / / /   ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 8)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / / / ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 9)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 10)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 2 ) and ( self.db.target.db.bashing == 11)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0
        
        
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X X X O O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / / O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 3)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / / / O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 4)):
                self.db.target.msg(prompt="|X|[wHealth: X X X / / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 5)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 6)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 7)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 3 ) and ( self.db.target.db.bashing == 8)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0


        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X O O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / / O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 3)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X / / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 4)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / / ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 5)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X / ")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 4 ) and ( self.db.target.db.bashing == 6)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0
        

        if((self.db.target.db.lethal == 5 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X O O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 5 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 5 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X / /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 5 ) and ( self.db.target.db.bashing == 3)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 5 ) and ( self.db.target.db.bashing == 4)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0                

        if((self.db.target.db.lethal == 6 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X O")
                self.db.target.db.conscious = 1
                
        if((self.db.target.db.lethal == 6 ) and ( self.db.target.db.bashing == 1)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X /")
                self.db.target.db.conscious = 0
                
        if((self.db.target.db.lethal == 6 ) and ( self.db.target.db.bashing == 2)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0
                

        if((self.db.target.db.lethal == 7 ) and ( self.db.target.db.bashing == 0)):
                self.db.target.msg(prompt="|X|[wHealth: X X X X X X X")
                self.db.target.db.conscious = 1
                self.db.target.db.alive = 0        


    def return_appearance(self, looker):
        looker.msg(image=[self.db.image, self.db.desc])

        def at_post_unpuppet(self, player, session=None):
            """
            We stove away the character when the player goes ooc/logs off,
            otherwise the character object will remain in the room also
            after the player logged off ("headless", so to say).
            Args:
            player (Player): The player object that just disconnected
                from this object.
            session (Session): Session controlling the connection that
                just disconnected.
            """
            if not self.sessions.count():
               # only remove this char from grid if no sessions control it anymore.
               if self.location:
                  self.location.for_contents(message, exclude=[self], from_obj=self)
                  self.db.prelogout_location = self.location
                  self.location = self.db.prelogout_location
                  self.ndb._menutree.close_menu()
                  self.db.target.ndb._menutree.close_menu()
