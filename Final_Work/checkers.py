import subprocess
import logging


def checkout(cmd, text):
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        if text in result.stdout and result.returncode == 0:
            return True, result.stdout  # Возвращаем результат
        else:
            return False, result.stdout  # Возвращаем результат
    except Exception as E:
        logging.error(f"Error executing command '{cmd}': {E}")
        return False, str(E)