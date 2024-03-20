import subprocess
from datetime import datetime
import os

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

def git_repository():
    link_repository = input("Ingresa link del repositorio: ")
    return link_repository

def git_init(directory):
    # Directory to start git
    os.chdir(directory)
    # Initialize the Git repository
    subprocess.run(['git', 'init'])

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
    # Improvable?
    subprocess.run(['git', 'push','--set-upstream', repository, 'master'])

def git_add_commit_push():
    subprocess.run(['git', 'add', '.'])
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Watakacraft [{formatted_date}]"
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

def main():

    option = input("¿Desea Agregar un nuevo repositorio (A) o Reinicializar repositorio (R)? ")
    
    if option == 'A':
        # Obtener la ruta del directorio del usuario
        directory = get_save_directory()
        git_init(directory)
        repository = git_repository()
        git_add_commit_push_first_time(repository)

    elif option == 'R':
        # Obtener la ruta del directorio del usuario
        directory = get_save_directory()
        git_init(directory)
        
        option = input("¿Desea Actualizar (A) o Guardar (G)? ").upper()
        
        if option == 'A':
            git_pull()
        elif option == 'G':
            git_add_commit_push()
        else:
            print("Opción no válida.")

    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()