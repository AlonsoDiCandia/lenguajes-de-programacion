class Demo:
    def set_password(self):
        self._password = input('Ingrese su contraseña: ')
    
    def get_password(self):
        print(f'La constraseña es: {self._password}')

class Person(Demo):
    def say_hello(self):
        print('Hello word!')
    
user = 'Pikachu'
demo = Demo()
demo.set_password()
demo.get_password()

person = Person()
person.say_hello()
person.get_password()


