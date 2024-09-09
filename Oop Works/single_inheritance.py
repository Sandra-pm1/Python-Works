class Vehicle:

    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def start(self):
        print(f"{self.name} Vehicle start method")

    def accelerate(self):
        print(f"{self.name} Vehicle accelerate method")


class Swift(Vehicle):

    def __init__(self,name,brand):
        super().__init__(name,brand)

swift_instance=Swift("swift","maruthy")

swift_instance.start()

swift_instance.accelerate() 