import subprocess
from datetime import datetime
import os

def save_directory(directory):
    try:
        with open('save_directory.txt', 'a') as file:
            file.write(directory + '\n')
        print("Ruta guardada correctamente.")
    except Exception as e:
        print(f"Error al guardar la ruta: {str(e)}")

def get_save_directory():
    save_dir_file = 'save_directory.txt'
    # Try to read the path from the file
    try:
        with open(save_dir_file, 'r') as file:
            save_directory = file.read().strip()
            if save_directory:
                return save_directory
            else:
                raise FileNotFoundError
    # If the file does not exist or is empty, prompt the user for the path
    except FileNotFoundError:
        save_directory = input("Ingresa la ruta del directorio de guardado: ")
        with open(save_dir_file, 'w') as file:
            file.write(save_directory)
        return save_directory
    
def show_saved_routes():
    save_dir_file = 'save_directory.txt'
    try:
        with open(save_dir_file, 'r') as file:
            rutas = file.readlines()
            if rutas:
                print("Rutas guardadas:")
                for i, ruta in enumerate(rutas, start=1):
                    print(f"{i}. {ruta.strip()}")
                return rutas
            else:
                print("No hay rutas guardadas en el archivo.")
                return []
    except FileNotFoundError:
        print("No se encontró el archivo de rutas guardadas.")
        return []

def git_repository():
    link_repository = input("Ingresa link del repositorio: ")
    return link_repository

def git_init(directory):
    # Directory to start git
    os.chdir(directory)
    # Initialize the Git repository
    subprocess.run(['git', 'init'])

def git_clone(repository):
    subprocess.run(['git', 'clone', repository])

def git_pull():
    # To update existing changes in the repository that are not local
    subprocess.run(['git', 'pull'])

def git_add_commit_push_first_time(repository):
    # To upload changes to the repository
    subprocess.run(['git', 'add', '.'])
    # Get date and time
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    # We customize the commit message plus the date and time
    commit_message = f"First commit Watakacraft [{formatted_date}]"
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push','--set-upstream', repository, 'master'])

def git_add_commit_push():
    # To upload changes to the repository
    subprocess.run(['git', 'add', '.'])
    # Get date and time
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    # We customize the commit message plus the date and time
    commit_message = f"Watakacraft [{formatted_date}]"
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

def main_menu():
    option = input("""
                Selecciona una opción:\n
                1. Agregar nuevo repositorio.
                2. Clonar repositorio.
                3. Reinicializar repositorio.\n
                \tIngresar opción: """)
    
    return option 

def main():
    opcion_elegida = main_menu()

    if opcion_elegida == '1':
        directory = input("Ingresa la ruta del directorio de quieres guardarlo: ")
        save_directory(directory)
        git_init(directory)
        repository = git_repository()
        git_add_commit_push_first_time(repository)

    elif opcion_elegida == '2':
        # The address where you want to clone the repository is defined
        directory = input("Ingresa la ruta del directorio de guardado: ")
        save_directory(directory)
        git_init(directory)
        repository = git_repository()
        git_clone(repository)

    elif opcion_elegida == '3':
        routes_option = input("""
                        1. Elegir ruta  
                        2. ingresar ruta\n
                           
                        \tIngresar opción:""")
        if routes_option == '1':
            rutas_guardadas = show_saved_routes()

            # Prompt the user to choose a route if there are saved routes
            if rutas_guardadas:
                sub_option = input("Elige una ruta ingresando su número o ingresa 0 para volver atrás: ")
                try:

                    opcion_numero = int(sub_option)
                    
                    if opcion_numero == 0:
                        # The user chose to go back
                        pass

                    elif 0 < opcion_numero <= len(rutas_guardadas):
                        # The user chose a valid route
                        ruta_elegida = rutas_guardadas[opcion_numero - 1].strip()
                        print(f"Has elegido la ruta: {ruta_elegida}")
                        git_init(ruta_elegida)

                        git_option = input("¿Desea Actualizar (A) o Guardar (G)? ").upper()

                        if git_option == 'A':
                            git_pull()
                        elif git_option == 'G':
                            git_add_commit_push()
                        else:
                            print("Opción no válida.")
                    else:
                        print("Opción no válida.")
                except ValueError:
                    print("Opción no válida. Ingresa un número válido.")
            else:
                print("Opción no válida.")
        elif routes_option == '2':
            directory = input("Ingresa la ruta del directorio de guardado: ")
            save_directory(directory)
            git_init(directory)
            git_add_commit_push()
        else:
            print("Opción no válida.")

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()