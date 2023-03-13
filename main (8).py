import csv
import datetime


#Pizza main class
class Pizza:
    
        
    def get_description(self):
        return self.__class__.__description__
    def get_cost(self):
        return self.__class__.cost
#subclasses derivated from Pizza


class ClassicPizza(Pizza):   
    cost=125
    def __init__(self):
        
        self.description="tomato_sauce,chese,olives and mushrooms"
        print(self.description)
   
     
      
        
class MargaritaPizza(Pizza):
    cost=120
    def _init_(self):
        self.description="tomato_sauce,mosarella chesee and basil"
        print(self.description)
    
    
       
     
class DominosPizza(Pizza):
    cost=156
    def _init_(self):
        description="meat,corn,olives,chesee,,mushrooms,onions"
        print(self.description)
   
    
        
    
class FumePizza(Pizza):
    cost=80
    def _init_(self):
        description="bacon and tomato_sauce"
        print(self.description)
    
    

      
################################################################################################################### 
#Decorator class which has Pizza class properties
class Decorator (Pizza):
    def __init__(self, ingredients):
        super().__init__()
        self.component = ingredients
        

    def get_cost(self):
        return self.component.get_cost() + \
               Pizza.get_cost(self)


    def get_description(self):
        return self.component.get_description() + \
        ' ' + Pizza.get_description(self)
        
    
        
 # subclasess that derivated from Decorator       
class Olives(Decorator):
    cost=8
    def __init__(self, ingredients):
        super().__init__(ingredients)
   
   
   
      
        
class meat (Decorator):
    cost=20
    def __init__(self, ingredients):
        super().__init__(ingredients)
    
    
    
        
       
class mushrooms(Decorator):
    cost=9
    def __init__(self, ingredients):
        super().__init__(ingredients)
    
class corn(Decorator):
    cost=5
    def __init__(self,ingredients):
        super().__init__(ingredients)
        
################################################################################################################
#main class    
    
    print("WELCOME TO PİZZA VALENCIA!!!")
    
    with open("Menu.txt","r") as file:
        for i in file:
            print(i,end=" ")
    
    
    
    
    Menu_dict={1:ClassicPizza,
               2:MargaritaPizza,
               3:DominosPizza,
               4:FumePizza,
               11:Olives,
               12:mushrooms,
               13:meat}
                  
    value= input("Please pick a pizza:")

    while value not in ["1","2","3","4"]:
        value=input("you entered invalid number!,please enter valid number")
                  
    order= Menu_dict[int(value)]()
           
    while value !="okay":
        value =input("if you wanna add any sauce,please enter a number, or you can enter okay to approve ")
        if value in ["11","12","13"]:
            order= Menu_dict[int(value)](order)
    print("\n"+";$"+str(order.get_cost()))
    print("\n")
        
    print("...............Customer Informations.............")
    
    name=input("Please enter your name :")
    Id=input("Please enter your Turkish ID :")
    if len(Id)==4:
         
   
       Credit_card=int(input("Please enter your credit card informations :"))
       Password=int(input("Please enter your card's password :"))
   
       time = datetime.datetime.now()
    
    
       with open('Orders_Database.csv', 'a') as file1:
            file1=csv.writer(file1,delimiter=',')
            file1.writerow([name, Id, Credit_card, order.get_description(), time])
            print("Order has approved.")
    
   