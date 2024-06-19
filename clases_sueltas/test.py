class Demo:
    def __password(self):
        print('Mi contraseña es: ajkbsdkja')
    
    def public(self):
        self.__password()

class Child(Demo):
    def __password(self):
        print('Mi contraseña es: 5555555555')
    
    # def public2(self):
    #     self.__password()

demo = Demo()
# demo.__password()
demo.public()

child = Child()
child.public()
child.public2()