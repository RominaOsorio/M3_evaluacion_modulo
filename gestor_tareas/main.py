# https://github.com/RominaOsorio/M3_evaluacion_modulo

from funciones import (
    cargar_tareas,
    mostrar_menu,
    agregar_tarea,
    ver_tareas,
    completar_tarea,
    eliminar_tarea,
)


def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("\nSaliendo del programa. ¡Hasta luego!\n")
            break
        else:
            print("\nOpción no válida, intenta nuevamente.")


if __name__ == "__main__":
    main()
