#create class
class Room:

    #create attributes of room
    length = 0.0
    Breadth = 0.0

    #Method to calculate area
    def calculate_area(self)
        print("The area of the  =",  self.length * self.Breadth)
    

#Instance of a class Room
study_room = Room()

#assigning values to attributes
study_room.length = 45
study_room.Breadth = 34

#Acessing the function within a class
study_room.calculate_area()
