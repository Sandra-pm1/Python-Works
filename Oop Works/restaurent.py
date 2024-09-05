class Dishes:
    name=str
    price=int
    quantity=str

    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __str__(self):
        return self.name



class Restaurent:
    name=str
    place=str

    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.dishes=[]

    def add_dishes(self,dish):
        self.dishes.append(dish)
    
    def list_dishes(self):
        for d in self.dishes:
            print(d)

biriyani_instance=Dishes("Biriyani",160,"half")
sharwarma_instance=Dishes("Sharwarma",120,"roll")
friedrice_instance=Dishes("Fried rice",140,"full")

restaurent_instance=Restaurent("Relax","Triprayar")

restaurent_instance.add_dishes(biriyani_instance)
restaurent_instance.add_dishes(sharwarma_instance)
restaurent_instance.add_dishes(friedrice_instance)
restaurent_instance.list_dishes()