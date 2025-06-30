class Persona:
    def __init__(self, name, age, hobbie, password):
        self.name = name
        self.age = age
        self.hobbie = hobbie
        self.password = password

        if len(password) < 3:
            print("Tu contraseña no debe tener menos de 3 caracteres")
        elif len(password) > 12:
            print("Tu contraseña no debe tener más de 12 caracteres")
        else:
            print(f"""
El nombre de la persona es: {self.name} y tiene {self.age} y le gusta {self.hobbie}
Su contraseña es {self.password}
""")


name = input("Ingresa un nombre: ")
age = input("Ingresa una edad: ")
hobbie = input("Ingresa algo que te guste: ")
password = input("Ingresa una contraseña: ")

Persona(name, age, hobbie, password)
