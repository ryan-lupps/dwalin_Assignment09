'''
#Name: Seth Medlin, Addyson Stansel, Ryan Lupton, Tyra __
#email: luptonrj@mail.uc.edu
#Assignment: Assignment 09
#Course: IS 4010
#Semester/Year: Fall 2022
#Brief Description: This project demonstrates that we can work together in a group to produce modular code
#Citations: 
#Anything else thats relevant: N/A
'''
class Rating():
    def setRating(self, rating):
        self.validateRating(rating)
    def validateRating(self, rating):
        if rating < 0:
            print ("A movie cannot be rated below 0")
        else:
            self.rating = rating
        if rating > 100:
            print ("A movie cannot be rated above 100")
        else:
            self.rating = rating 
             
    def __init__(self, movieTitle, rating):
        self.movieTitle = movieTitle  
        self.validateRating(rating)
       
    def __repr__(self):
        return "Score: " + self.movieTitle + self.rating
    
    def __str__(self):
        return "Score: " + self.movieTitle + str(self.rating) 
