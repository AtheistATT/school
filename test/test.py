import questionary
import pdb
import os
import random

class question:
    q_title = ""
    q_right_ansver = ""
    q_choise = []

    def __init__(self, q_str) -> None:
       q_list = q_str.split('|')
       self.q_title = q_list.pop(0)
       self.q_right_ansver = q_list[0]
       random.shuffle(q_list)
       self.q_choise = q_list

    def ask(self):
        u_choise = questionary.select(self.q_title, choices=self.q_choise).ask()
        if u_choise == self.q_right_ansver:
            return True
        else:
            return False





data_path = "./data/hiden/"
file_list = os.listdir(data_path)
test = ""

test_file = questionary.select("Выберите название теста.",choices=file_list).ask()

with open(data_path + test_file, "r", encoding='utf-8') as file:
    test = file.read()

test = test.split('\n')
title = test.pop(0)
input(title + "\nДля продолжения нажмите любую клавишу...")

test.pop()
q_max = len(test)
q_user_right = 0

for q in test:
    quest = question(q)

    if quest.ask():
        q_user_right += 1

print(f"{q_user_right}/{q_max} {q_user_right/q_max * 100}%")





input("Программа завершена. Для продолжения нажмите любую клавишу...")
