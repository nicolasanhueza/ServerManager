import subprocess
from datetime import datetime

def git_init():
    subprocess.run(['git', 'init'])

def git_pull():
    subprocess.run(['git', 'pull'])

def git_add_commit_push():
    subprocess.run(['git', 'add', '.'])
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"Watakacraft [{formatted_date}]"
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push'])

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