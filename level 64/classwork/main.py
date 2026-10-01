# Multi-level inheritance

# შექმენით კლასი Gadgets, რომელსაც ეყოლება შვილი კლასი Phone-ი. 
# აიღეთ Phone კლასი, დაუმატეთ რამდენიმე თვისება და ერთი მეთოდი, რომელიც გამოიტანს:
#     'Calling'-ს. და მშობელ კლასად გადაეცით Ios და Android კლასებს

class Gadgets:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        
        
        
class Phone:
    def __init__(self,brand,color,model):
        super().__init__(self,brand,color)
        self.model = model
    
    def calling(self):
        print("Phone is calling")
        
        
        
        
        
laptop = Gadgets("Asus" ,"Black")    
        
phone = Phone("Iphone","Blue","iphon 13 pro max")   




     
# Multiple Level Inheritence

# შექმენით კლასი VacuumCleaner, რომელსაც ექნება Vacuum მეთოდი.
# ასევე, შექმენით Robot კლასი, რომელსაც ექნება DetectObstacle მეთოდი.

# საბოლოოდ, შექმენით RobotVacuum კლასი, რომელიც მიიღებს VacuumCleaner და Robot -ის მეთოდებს მემკვიდრეობით.


class VacuumCleaner:
    def vaccuum(self):
        print("Vacuuming")
        
        
        
class Robot:
    def robot(self):
        print("Detecting Obstacles")
        
class RobotVacuum(VacuumCleaner , Robot):
    pass
    
    
 
RobVacuum =  RobotVacuum()  

RobVacuum.vaccuum()

RobVacuum.robot()