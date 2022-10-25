'''
#Name: Seth Medlin, Addyson Stansel, Ryan __, Tyra __
#email: medlinsh@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work together in a group to produce modular code
#Citations: 
#Anything else thats relevant: N/A
'''

# Shrek - $487.9 million
# Shrek 2 - $928.7 million
# Shrek the Third - $813.4 million
# Shrek Forever After - $752.6 million
# Puss in Boots - $555 million

#Dictionary containing box office profits (in Millions)
boxOfficeProfits = {'Shrek': 487.9,
                    'Shrek 2': 928.7,
                    'Shrek the Third': 813.4,
                    'Shrek Forever After': 752.6,
                    'Puss in Boots':555
                    }


class boxPerformance():
    
    def movieCheck(self,film):
        #check that the film in in the dictionary
        if any(str(film) in l for l in boxOfficeProfits.values()):
                self.film = film
        else:
                print("That film is not in the repository. Only " + str(boxOfficeProfits) + " are available.")
            
    
        

    # Defining film repository
    def __init__(self,film):
        self.movieCheck(film) #checking the shoe is a type we stock
        self.film = film #store the film name in the current object
        
        
        
    def __repr__(self):
        # Returns a string representation of the project
        return "Film = " + self.film
    
    
    def __str__(self):
        return "The film's box office profits were: " + str((self.film) in l for l in boxOfficeProfits.values())


