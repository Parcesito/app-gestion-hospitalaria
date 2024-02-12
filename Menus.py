import time
from os import system
from Classes import Medical_History, Bed
import Functions


def welcome():
    print("==========================================================\n")
    print("      Bienvenido al sistema de gestión hospitalaria,      ")
    print("                           doctor                         \n\n\n")
    print("==========================================================")
    time.sleep(2)
    system("cls")


def first_submenu(pacientes: list[Medical_History], altas, servicios, admisiones, dias_estancia, beds):
    visor = 1
    bandera = 0
    while visor != 0:
        print("================== Gestión de pacientes ===================")
        print("1 - Añadir paciente")
        print("2 - Dar de alta a paciente")
        print("3 - Agregar nota al paciente")
        print("4 - Nueva enfermedad crónica detectada")
        print("5 - Revisar historia médica")
        print("6 - Volver al menú principal ")
        print("===========================================================")
        visor = int(input("Por favor, ingrese el número relacionado a la opción que desea ejecutar: "))
        system("cls")

        if visor == 1:
            pacientes.append(Functions.new_historial(beds))
            time.sleep(2)
            system("cls")
            servicios += 1
            admisiones += 1

        elif visor == 2:
            visor = input("Por favor,ingrese la identificación del paciente al que va a dar de alta: ")
            for i in range(len(pacientes)):
                if pacientes[i].patient.document == visor:
                    pacientes.pop(i)
                    dias_estancia += float(input("Por favor, ingrese la la cantidad de días que estuvo internado: "))
                    altas += 1
                    print("===========================================================")
                    bandera = 1
                    break
            if bandera == 0:
                print("===========================================================\n")
                print("      La identificación no coincide con ningún paciente")
                print("                 Ingresado en el sistema\n")
                print("===========================================================")
                time.sleep(2)
                system("cls")
            bandera = 0

        elif visor == 3:
            visor = Functions.validate_interger(visor,
                                                "Por favor,ingrese la identificación del paciente: ")
            note = ''
            for i in range(len(pacientes)):
                if pacientes[i].patient.document == visor:
                    note = input("Por favor, escriba la nota que desea guardar en el registro del paciente: ")
                    pacientes[i].notes.new_note(note)
                    print("===========================================================")
                    bandera = 1
                    break
            if bandera == 0:
                print("===========================================================\n")
                print("      La identificación no coincide con ningún paciente")
                print("                 Ingresado en el sistema\n")
                print("===========================================================")
                time.sleep(2)
                system("cls")
            bandera = 0

        elif visor == 4:
            visor = Functions.validate_interger(visor,
                                                "Por favor,ingrese la identificación del paciente: ")
            note = ''
            for i in range(len(pacientes)):
                if pacientes[i].patient.document == visor:
                    note = input("Por favor, escriba la nueva enfermedad que desea guardar registro del paciente: ")
                    pacientes[i].notes.new_disease(note)
                    print("===========================================================")
                    bandera = 1
                    break
            if bandera == 0:
                print("===========================================================\n")
                print("      La identificación no coincide con ningún paciente")
                print("                 Ingresado en el sistema\n")
                print("===========================================================")
                time.sleep(2)
                system("cls")
            bandera = 0
        elif visor == 5:
            visor = Functions.validate_interger(visor,
                                                "Por favor,ingrese la identificación del paciente que desea revisar:")
            system("cls")
            for i in range(len(pacientes)):
                if pacientes[i].patient.document == visor:
                    pacientes[i].print_history()
                    bandera = 1
                    break
            if bandera == 0:
                print("===========================================================\n")
                print("      La identificación no coincide con ningún paciente")
                print("                 Ingresado en el sistema\n")
                print("===========================================================")
                time.sleep(2)
                system("cls")
            bandera = 0
        elif visor == 6:
            visor = 0
            print("===========================================================\n")
            print("                 Regresando al menú principal\n")
            print("===========================================================")
            time.sleep(2)
            system("cls")


def second_submenu(pacientes, altas, servicios, admisiones, dias_estancia, beds):
    c_diseases = 0
    meds_count = 0
    for i in range(len(pacientes)):
        c_diseases += len(pacientes[i].notes.chronic_diseases) - 1
        meds_count += len(pacientes[i].recipe.medicines) - 1
    cont = 0
    for i in range(len(beds)):
        for j in range(len(beds[i])):
            if beds[i][j].ocupated:
                cont += 1
    if servicios == 0:
        print("===========================================================\n")
        print("               No se han realizado servicios,              ")
        print("       Por lo que no es posible imprimir indicadores       \n")
        print("===========================================================")
        time.sleep(2)
        system("cls")
    else:
        print("===================== Indicadores =========================")
        print(f'Admisiones por servicio: {admisiones / servicios}')
        print(f'Altas por servicio: {altas / servicios}')
        print(f"Estancia promedio: {dias_estancia / servicios}")
        print(f'Ocupación hospitalaria: {(cont / 300) * 100}')
        print(f'Medicamentos preescritos por servicio: {meds_count / servicios}')
        print(f'Cantidad de pacientes con enfermedades crónicas: {c_diseases}')
        print("Identificaciones de pacientes con enfermedades crónicas: ")
        for i in range(len(pacientes)):
            if len(pacientes[i].notes.chronic_diseases) > 1:
                print(f'{pacientes[i].patient.document}')
        print("===========================================================")
        input("Ingrese cualquier valor para volver al menú principal. ")
        time.sleep(2)
        system("cls")


def main_menu():
    pacientes: list[Medical_History] = []
    altas = 0
    servicios = 0
    dias_estancia = 0.0
    admisiones = 0
    beds: list[list[Bed]] = []
    Functions.fill_beds(beds)
    case = 0
    while True:
        print("=================== Menú principal =======================\n")
        print("1 - Gestión de pacientes. ")
        print("2 - diagrama de camas. ")
        print("3 - Impresión de indicadores. ")
        print("4 - Finalizar el programa. ")
        print("==========================================================")
        case = Functions.validate_interger(case,
                                           "Por favor, ingrese el número relacionado a la opcion que desea ejecutar")

        if case == 1:
            first_submenu(pacientes, altas, servicios, admisiones, dias_estancia, beds)

        elif case == 2:
            Functions.print_beds(beds)

        elif case == 3:
            second_submenu(pacientes, altas, servicios, admisiones, dias_estancia, beds)

        elif case == 4:
            print("===========================================================\n")
            print("           ¡Muchas gracias por utilizar el programa! \n")
            print("===========================================================")
            break
        else:
            print("===========================================================\n")
            print("    El valor ingresado es inválido, inténtelo nuevamente \n")
            print("===========================================================")
