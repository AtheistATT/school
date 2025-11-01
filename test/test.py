'''
Это моя программа для проведения тестов!
И она работает!
'''
import questionary
#import pdb
import os
import random
import datetime

class question:
    def __init__(self, q_str) -> None:
       q_list = q_str.split('|')
       self.q_title = q_list.pop(0)
       self.q_right_ansver = q_list[0]
       random.shuffle(q_list)
       self.q_choise = q_list
       self.u_choise = ''

    def ask(self):
        self.u_choise = questionary.select(self.q_title, choices=self.q_choise, instruction="⬆️ ⬇️ ↩️.").ask()
        if self.u_choise == self.q_right_ansver:
            return True
        else:
            return False





data_path = "./data/hiden/"
file_list = os.listdir(data_path)
last = ''
user_name = ''
detals_log = ''

test_file = questionary.select("Выберите название теста.",choices=file_list, instruction="⬆️ ⬇️ ↩️").ask()
q_size = int(input("Выберете количество вопросов в тесте\n>>>"))
mark = input("Введите название класса\n>>>")

detals_log = mark + '\n'

while True:
    os.system('clear')
    with open(data_path + test_file, "r", encoding='utf-8') as file:
        test = file.read()

    test = test.splitlines()
    title = test.pop(0)

    if q_size < 1:
        q_size = 1

    if q_size > len(test):
        q_size = len(test)


    print(last)
    user_name = input(title + "\nВведите фамилию ↩️ >>>")

    detals_log +=  user_name + '\n'

    random.shuffle(test)
    test = test[:q_size]

    q_max = len(test)
    q_user_right = 0

    for q in test:
        quest = question(q)

        if quest.ask():
            q_user_right += 1
            detals_log += ' + '  
        else:
            detals_log += ' - '  
        detals_log += quest.q_title + '(' + quest.q_right_ansver + ') Ваш ответ:'+ quest.u_choise +'\n'

    log_str = f"{mark} {test_file} {user_name} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {q_user_right}/{q_max} {q_user_right/q_max * 100:.1f}%"
    print(log_str)
    last = log_str

    with open("data/log.txt", 'a', encoding='utf-8') as file:
        file.write(log_str + '\n')
    with open("data/log_d.txt", 'a', encoding='utf-8') as file:
        file.write(detals_log + '\n')


    input("Для продолжения нажмите ENTER...")
