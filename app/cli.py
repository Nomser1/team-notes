from app.notes import add_note, list_notes

def main():
    while True:
        print("\n--- Team Notes CLI ---")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("0. Salir")
        choice = input("Opción: ")

        if choice == "1":
            title = input("Título: ")
            content = input("Contenido: ")
            add_note(title, content)
            print("✅ Nota agregada.")
        elif choice == "2":
            notes = list_notes()
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note['title']}: {note['content']}")
        elif choice == "0":
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
    