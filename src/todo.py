"""
Aplicación de lista de tareas (TODO) simple en Python.
"""

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
        json.dump(tareas, f, ensure_ascii=False, indent=2)


def agregar_tarea(descripcion):
    tareas = cargar_tareas()
    tarea = {
        "id": len(tareas) + 1,
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    print(f"✅ Tarea agregada: {descripcion}")


def listar_tareas():
    tareas = cargar_tareas()
    if not tareas:
        print("📋 No hay tareas pendientes.")
        return
    print("\n📋 Lista de Tareas:")
    print("-" * 40)
    for t in tareas:
        estado = "✔" if t["completada"] else "○"
        print(f"  [{estado}] {t['id']}. {t['descripcion']}")
    print("-" * 40)


def completar_tarea(id_tarea):
    tareas = cargar_tareas()
    for t in tareas:
        if t["id"] == id_tarea:
            t["completada"] = True
            guardar_tareas(tareas)
            print(f"✔ Tarea {id_tarea} marcada como completada.")
            return
    print(f"❌ No se encontró la tarea con ID {id_tarea}.")


def eliminar_tarea(id_tarea):
    tareas = cargar_tareas()
    nuevas = [t for t in tareas if t["id"] != id_tarea]
    if len(nuevas) == len(tareas):
        print(f"❌ No se encontró la tarea con ID {id_tarea}.")
    else:
        guardar_tareas(nuevas)
        print(f"🗑 Tarea {id_tarea} eliminada.")


def menu():
    print("\n=== TODO App ===")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    return input("Opción: ").strip()


def main():
    while True:
        opcion = menu()
        if opcion == "1":
            desc = input("Descripción de la tarea: ").strip()
            if desc:
                agregar_tarea(desc)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            listar_tareas()
            try:
                id_t = int(input("ID de la tarea a completar: "))
                completar_tarea(id_t)
            except ValueError:
                print("❌ Ingresá un número válido.")
        elif opcion == "4":
            listar_tareas()
            try:
                id_t = int(input("ID de la tarea a eliminar: "))
                eliminar_tarea(id_t)
            except ValueError:
                print("❌ Ingresá un número válido.")
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    main()
