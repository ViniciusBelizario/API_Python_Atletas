import subprocess
import os

def start_uvicorn():
    subprocess.run(["uvicorn", "workout_api.main:app", "--reload"])

def create_migrations():
    command = f"set PYTHONPATH=%PYTHONPATH%;{os.getcwd()} && alembic revision --autogenerate -m \"$(d)\""
    subprocess.run(command, shell=True)

def run_migrations():
    command = f"set PYTHONPATH=%PYTHONPATH%;{os.getcwd()} && alembic upgrade head"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    create_migrations()
    run_migrations()
    start_uvicorn()
