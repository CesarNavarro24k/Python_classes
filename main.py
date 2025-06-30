class Persona:
    def __init__(self, name, age, hobbie, password, user):
        self.name = name
        self.age = age
        self.hobbie = hobbie
        self.password = password
        self.user = user

        if len(password) <= 3:
            print("Tu contraseña no debe tener menos de 3 caracteres")
        elif len(password) > 3 and len(password) <= 12:
            print("Tu contraseña no debe tener más de 12 caracteres")
        else:
            print(f"""
El nombre de la persona es: {self.name} y tiene {self.age} y le gusta {self.hobbie}
Su contraseña es {self.password} y su nombre de usuario es: {user}
""")


name = input("Ingresa un nombre: ")
age = input("Ingresa una edad: ")
hobbie = input("Ingresa algo que te guste: ")
password = input("Ingresa una contraseña: ")
user = input("Ingresa tu nombre de usuario:")


Persona(name, age, hobbie, password, user)
