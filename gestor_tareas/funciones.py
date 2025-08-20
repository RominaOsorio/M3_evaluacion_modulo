# https://github.com/RominaOsorio/M3_evaluacion_modulo

import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)


def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def agregar_tarea(tareas):
    nombre = input("Escribe la tarea: ").strip()
    if nombre:
        tareas.append({"nombre": nombre, "estado": "Pendiente"})
        guardar_tareas(tareas)
        print("\nTarea agregada con éxito.")
    else:
        print("\nLa tarea no puede estar vacía.")


def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas registradas.")
    else:
        print("\n--- Lista de Tareas ---")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea['nombre']} - [{tarea['estado']}]")


def completar_tarea(tareas):
    ver_tareas(tareas)
    if tareas:
        try:
            i = int(input("Número de tarea a completar: ")) - 1
            if 0 <= i < len(tareas):
                tareas[i]["estado"] = "Completada"
                guardar_tareas(tareas)
                print("\nTarea marcada como completada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Ingresa un número válido.")


def eliminar_tarea(tareas):
    ver_tareas(tareas)
    if tareas:
        try:
            i = int(input("Número de tarea a eliminar: ")) - 1
            if 0 <= i < len(tareas):
                tarea = tareas.pop(i)
                guardar_tareas(tareas)
                print(f"\nTarea '{tarea['nombre']}' eliminada.")
            else:
                print("Número de tarea inválido.")
        except ValueError:
            print("Ingresa un número válido.")
