import subprocess
from datetime import datetime
import os

def get_save_directory():
    home_directory = os.path.expanduser("~")
    # World route
    return os.path.join(home_directory, "AppData", "Roaming", ".minecraft", "essential_mod", "forge", "1.20.1", "1.20.1 Forge Essential", "saves", "New World")

def git_init(directory):
    # Directory to start git
    os.chdir(directory)
    # Initialize the Git repository
    subprocess.run(['git', 'init'])

def git_pull():
    # To update existing changes in the repository that are not local
    subprocess.run(['git', 'pull'])

def git_add_commit_push():
    # To upload changes to the repository
    subprocess.run(['git', 'add', '.'])
    # Get date and time
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    # We customize the commit message plus the date and time
    commit_message = f"Watakacraft [{formatted_date}]"
    subprocess.run(['git', 'commit', '-m', commit_message])
    # Improvable?
    subprocess.run(['git', 'push', '--set-upstream', 'https://github.com/nicolasanhueza/MundoPrueba.git', 'master'])
    
def main():
    git_init()
    option = input("¿Desea Actualizar (A) o Guardar (G)? ").upper()
    if option == 'A':
        git_pull()
    elif option == 'G':
        git_add_commit_push()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()