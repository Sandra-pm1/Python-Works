class Vehicle:
    name=str
    brand=str
    price=int

    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    
    def __str__(self):
        return self.name

class Showroom:
    name=str
    place=str

    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.vehicle=[]

    def add_vehicle(self,vehicle):
        self.vehicle.append(vehicle)

    def list_vehicle(self):
        for v in self.vehicle:
            print(v)

hunter_instance=Vehicle("Hunder","RE",100000)
activa_instance=Vehicle("Activa","Honda",80000)
himalayaln_instance=Vehicle("Himalayan","RE",150000)

showroom_instance=Showroom("TrueValue","Edappally")

showroom_instance.add_vehicle(hunter_instance)
showroom_instance.add_vehicle(activa_instance)
showroom_instance.add_vehicle(himalayaln_instance)
showroom_instance.list_vehicle()