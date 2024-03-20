import subprocess
from datetime import datetime
import os

def git_init():
    # Cambiar al directorio deseado
    os.chdir(r'C:\Users\nicol\AppData\Roaming\.minecraft\essential_mod\forge\1.20.1\1.20.1 Forge Essential\saves\New World')
    # Inicializar el repositorio Git
    subprocess.run(['git', 'init'])

def git_pull():
    subprocess.run(['git', 'pull'])

def git_add_commit_push():
    subprocess.run(['git', 'add', '.'])
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Watakacraft [{formatted_date}]"
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push', '--set-upstream', 'https://github.com/nicolasanhueza/MundoPrueba.git', 'master'])
def main():
    git_init()
    option = input("¿Desea actualizar (U) o guardar (G)? ").upper()
    if option == 'U':
        git_pull()
    elif option == 'G':
        git_add_commit_push()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()