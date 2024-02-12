from Classes import Patient, Bed, Medical_History, Recipe, Notes, Images
from colorama import init, Fore
from datetime import date


def fill_beds(vector):
    provisional = []
    for i in range(20):  # Se llena la lista provicional con 10 espacios
        vector.append([])
        for j in range(15):
            vector[i].append(Bed(i, j, False))


def print_beds(vector):
    init(autoreset=True)  # Después de cada cadena impresa a color, volverá a blanco.
    cont = 0
    for i in range(len(vector)):
        for j in range(len(vector[i])):
            if vector[i][j].ocupated:
                cont += 1
    print(Fore.GREEN + f'Desocupadas: {300-cont}')
    print(Fore.RED + f'Ocupado: {cont}')

    for i in range(len(vector)):
        print("[   ", end='')
        for j in range(len(vector[i])):
            if vector[i][j].ocupated:
                print(Fore.RED + f'*\t', end='')
            else:
                print(Fore.GREEN + f'*\t', end='')
        print(f']')


def validate_interger(value, name):
    while True:
        try:
            value = int(input(name))

        except ValueError:
            print("El valor es inválido")
            continue
        return value


def new_historial(vector):
    column = -1
    file = -1
    bandera = 0
    name = input("Por favor, ingrese el nombre completo del paciente")
    document = 0
    birthday = 0
    sexo = ''

    while True:
        try:
            birthday = date.fromisoformat(input("Por favor, ingrese la fecha de nacimiento del paciente en formato YYYY-MM-DD: "))

        except ValueError:
            print("Ha ingresado un valor erróneo, por favor inténtelo nuevamente")
            continue
        break

    while True:
        try:
            document = int(input("Por favor, ingrese su documento de identidad, no utilice puntos ni comas: "))

        except ValueError:
            print("El valor ingresado es inválido, por favor inténtelo nuevamente")
            continue
        break
    document = str(document)
    print("Este es el diagrama de camas disponibles: ")
    print_beds(vector)

    while True:
        while column < 0 or column > 20:
            column = validate_interger(column, "Por favor, ingrese el valor de la columna de la cama que desea asignar: ")
        while file < 0 or file > 15:
            file = validate_interger(file, "Por favor, ingrese el valor de la fila de la cama que desea asignar: ")
        if vector[column][file].ocupated:
            print("La cama está ocupada, por favor inténtelo nuevamente")
        else:
            break

    while bandera == 0:
        print("Por favor, responda con el número relacionado al sexo del paciente: \n1. Masculino   2. Femenino")
        bandera = int(input("Respuesta: "))
        if bandera == 1:
            sexo = "Masculino"
        elif bandera == 2:
            sexo = "Femenino"
        else:
            print("Valor inválido, por favor inténtelo nuevamente")
            bandera = 0
    patient = Patient(document, name, sexo, birthday)
    recipe = Recipe()
    note = Notes()
    bed = vector[column][file]
    images = Images()
    aux = Medical_History(patient, recipe, note, bed, images)
    return aux
