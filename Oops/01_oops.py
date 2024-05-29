# here we have class and constructor!
#  we have to provide Context in Constructor Ok so we can Provide to instance it's own Context!
class Car:
    # this is constructor right when you create a new Instace this constructor calls first!
    def __init__(self,usermodel,userbrand):
        # self means we need to define context of each Instace!
        self.brand = userbrand
        self.model = usermodel
        
        # here we are defining fuctionalities of the Page!
    def Model_name(self):
        # when you create a new fucntionality so provide first context ok!
        return f"you car brand is {self.brand} and model is {self.model}"
        
my_car_suzuki = Car("suzuki","Brezza")
print(my_car_suzuki.brand)
print(my_car_suzuki.model)
# here we need to call functionality!
print(my_car_suzuki.Model_name())

my_car_safari = Car("Toyota","safari");
print(my_car_safari.brand)
print(my_car_safari.model)

