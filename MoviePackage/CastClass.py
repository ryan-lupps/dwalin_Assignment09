#Dictionary containing cast names
CastNames = { "Shrek": "Shrek:Mike Myers, Donkey: Eddie Murphy, Princess Fiona: Cameron Diaz, Lord Farquaad: John Lithgow",
        "Shrek2": "Queen: Julie Andrews, Puss In Boots: Antonio Banderas, King: John Cleese, Prince Charming: Rupert Everett",
        "ShrekTheThird": "Merlin: Eric Idle, Artie: Justin Timberlake, Evil Queen: Susanne Blakeslee, Pinocchio: Cody Cameron",
        "ShrekForeverAfter": "Brogan: John Hamm, Patrol Witch: Lake Bell, Dancing Witch: Kathy Griffin, Guard Witch: Mary Kay Place",
        "PussInBoots": "Puss in Boots: Antonio Banderas, Kitty Softpaws: Salma Hayek, Jack: Billy Bob Thornton, Jill: Amy Sedaris"
            }

class Cast():

    def CastCheck(self, name):
        if name in CastNames:
           print("The following actors were featured in this film: " + CastNames[name])
           
        else:
            print("That name is not in the cast list. Only " + str(CastNames) + " are available.")
       
   
    def __init__(self, name):
       self.CastCheck(name)  
       self.name = name
   
    def __repr__(self):
        return "Actors = " + self.name
   
    def __str__(self):
       return "The following actors were featured in this film: " + CastNames["Shrek"] in CastNames.values()
       
if __name__=="__main__":
    test = Cast("Shrek")
    test2 = Cast("Shrek2")
    test3 = Cast("ShrekTheThird")
    test4 = Cast("ShrekForeverAfter")
    test5 = Cast("PussInBoots")
   
    print(test.__str__())
