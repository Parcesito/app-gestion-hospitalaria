# Declaración de clases
import datetime as dt
from datetime import date

class Bed:
    def __init__(self, column: int, file: int, ocupated: bool):
        self.column = column
        self.file = file
        self.ocupated = ocupated

    def occupy(self):
        self.ocupated = not self.ocupated

    def occupied(self):
        return self.ocupated

    def __str__(self):
        f = f'El paciente ocupa la cama: [{self.column}]-[{self.file}]'
        return f


class Patient:  # The object stores patient information
    def __init__(self, document: str, name: str, sex: str, birthdate: date):
        self.document = document
        self.name = name
        self.sex = sex
        self.birthdate = birthdate


    def __str__(self):
        texto = (f'Nombre: {self.name}\nDocumento: {self.document}\nFecha de nacimiento: {self.birthdate} '
                 f'\nSexo: {self.sex} \n')
        return texto




class Notes:
    def __init__(self):
        self.evolution_notes: list[str] = ["Notas de evolución \n"]
        self.chronic_diseases: list[str] = ["Enfermedades crónicas padecidas \n"]

    def __str__(self):
        for i in range(len(self.evolution_notes)):
            print(self.evolution_notes[i])
        f = ''
        return f

    def new_note(self, note: str):
        self.evolution_notes.append('[' + str(dt.date.today()) + '] ' + note)

    def new_disease(self, disease: str):
        self.chronic_diseases.append(disease)

    def print_notes(self):
        for i in range(len(self.evolution_notes)):
            print(self.evolution_notes[i])
        for i in range(len(self.chronic_diseases)):
            print(self.chronic_diseases[i])


class Recipe: # Contendrá la lista de medicamentos recetados
    def __init__(self):
        self.medicines: list[str] = ["Medicamentos recetados \n"]

    def add_medicine(self, medicine: str):
        self.medicines.append(medicine)

    def __str__(self):
        for i in range(len(self.medicines)):
            print(self.medicines[i])
        f = ''
        return f


class Images:
    def __init__(self):
        self.names: list[str] = []
        self.directions: list[str] = []

    def add_image(self):
        self.names.append(input("Por favor, indique el nombre del diagnóstico"))
        self.directions.append(input("Por favor, indique la dirección del diagnóstico"))

    def __str__(self):
        for i in range(len(self.names)):
            print(f'{self.names[i]} : {self.directions[i]}')
        f=''
        return f

class Vital_Signs:
    def __init__(self):
        self.arterial_press: float = 0.0
        self.temperature: float = 0.0
        self.saturation: float = 0.0
        self.respiration: float = 0.0

class Medical_History:  # La clase contendrá toda la información de un paciente
    def __init__(self, patient: Patient, recipe: Recipe, notes: Notes, bed: Bed, images: Images ):
        self.patient = patient
        self.recipe = recipe
        self.notes = notes
        self.bed = bed
        self.images = images

    def print_history(self):
        print('==================== Historial médico ====================')
        print("Información personal")
        print(self.patient)
        title = '='
        print("==========================================================")
        print(self.recipe)
        print("==========================================================")
        self.notes.print_notes()
        print("==========================================================")
        print("Imágenes almacenadas")
        print(self.images)
        print("==========================================================")
        print(self.bed)



