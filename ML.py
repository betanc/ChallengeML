import subprocess

def ejecutar(script):
    try:
        subprocess.check_call(['python', script])
        print(f'Script {script} ejecutado.')
    except subprocess.CalledProcessError as e:
        print(f'Error {script}: {e}')

# scripts para bd
ejecutar('consumirserv.py')
ejecutar('parselscript.py')
ejecutar('auth.py')