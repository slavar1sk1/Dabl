# Импорт необходимых библиотек
import re
import time
import requests
from playsound import playsound
import pygetwindow as gw
from config_dabl import *
import pyautogui, pyttsx3, json, vosk, pyaudio, webbrowser, os, pyperclip
from random import choice
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import subprocess
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from dablwindow import Ui_Form
from pymongo import MongoClient
import sign_dabl
from bs4 import BeautifulSoup
import commands_win
import speech_recognition
import add_commands
# import openai

# Инициализация текстового движка
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty("voice", "ru")

# Выбор голоса "Elena" для синтеза речи
for voice in voices:
    if voice.name == 'Aleksandr':
        tts.setProperty("voice", voice.id)

# Инициализация подключения к MongoDB
cluster = MongoClient()
db_con = cluster["dabl_voice"]
collect = db_con["users_info"]

# Пути к моделям и настройкам распознавания речи
model_vosk = r"C:\pythonProject10\pythonProject3\vosk_model_small"
model = vosk.Model(model_vosk)
sample_rate = 16000
chunk_size = 1024

# Инициализация аудио-потока для записи звука
audio = pyaudio.PyAudio()
audio_stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True,
                          frames_per_buffer=chunk_size)

# Инициализация распознавателя речи
recognizer = vosk.KaldiRecognizer(model, sample_rate)

# Флаги работы программы
work = True
mir = False

# Переменные для хранения логина, пароля и команд JSON
login = None
password = None
json_commands = None

# Функция для загрузки задач из файла tasks.json
def dabl_commands() -> dict:
    """
    Загружаем задачи из файла tasks.json
    :return: Словарь с задачами
    """
    with open('tasks.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Функция для обработки текста пользователя
def find_user_text(text: str) -> list:
    text = text.lower().replace('{', '').replace('}', '').replace('"', '').replace("text", '').replace(":", '').replace(
        '\n', '').split(' ')
    return text

# Класс для работы с рабочим столом
class Desktop:
    # Функция для смены языка клавишей "Alt+Shift"
    def change_language(self):
        """
        Смена языка клавишей "Alt+Shift"
        """
        # Воспроизведение случайного звука из списка maked_task
        playsound(choice(maked_task))
        # Имитация нажатия клавиш "Alt+Shift"
        pyautogui.hotkey('alt', 'shift')

    # Функция для изменения громкости звука
    def change_voice(self, task: str):
        """
        Изменение громкости звука
        :param task: Команда с уровнем громкости
        """
        # Загрузка команд из файла tasks.json
        commands = dabl_commands()['commands']

        # Обработка текстовой команды, извлечение числа (громкости)
        task = (find_user_text(task))
        print(task)
        voice_number = ' '.join([i for i in task if i in number_dict.keys()])

        # Получение объекта устройства вывода звука
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        print('--------------')
        print(voice_number)
        # Установка громкости
        volume.SetMasterVolumeLevelScalar(float(f'0.{number_dict[voice_number]}'), None)



class Music:
    def open_music(self, task: str):
        """
        Открывает музыкальное приложение и воспроизводит указанную песню.
        :param task: Задача, содержащая информацию о включении музыки.
        """
        text = find_user_text(task)
        song = [i for i in task if i not in ['включи песню', 'включи музыку']]

        print('-' * 100)
        print(song)

class OpeningClosing:
    # Функции для открытия и закрытия различных приложений

    def opening_link(self, by_url: str, standart_voice: bool):
        """
        Открывает браузер и переходит на YouTube.
        :param by_url: URL YouTube.
        """
        if standart_voice:
            playsound(choice(opening_task))
        else:
            pass
        webbrowser.open(by_url)

    def opening_url(self, url: str, standart_voice: bool):
        """
        Открывает задачу.
        :param url: Путь к задаче.
        """
        if standart_voice:
            playsound(choice(opening_task))
        else:
            pass
        os.system(url)

    def closing_task(self, name: str):
        """
        Закрывает приложение по имени.
        :param name: Имя приложения.
        """
        playsound(choice(maked_task))
        windows = gw.getWindowsWithTitle(name)
        window = windows[0]
        window.close()

class Youtube:
    def __init__(self):
        self.commands_dict = dabl_commands()['commands']

    # Функция для поиска текста и ввода его в поле поиска

    def search(self, task: str, x: int, y: int):
        """
        Выполняет поиск текста и вводит его в поле поиска.
        :param task: Текст для поиска.
        :param x: Координата x.
        :param y: Координата y.
        """
        task = (task.lower().replace('{', '').replace('}', '').replace('"', '').replace("text", '')
                .replace(":", '').replace('\n', '').split(' '))

        sw = None
        for i in range(len(task)):
            if task[i].capitalize() in self.commands_dict['write']:
                sw = i

        task2 = ' '.join(task[sw + 1:])

        try:
            playsound(r"C:\pythonProject10\pythonProject3\Dabl\vioce\how_say.mp3")
        except:
            pass
        pyautogui.click(x, y)
        time.sleep(1)
        print(task2)
        pyperclip.copy(task2)
        time.sleep(0.1)
        pyperclip.copy(task2)
        time.sleep(1.5)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

        time.sleep(0.5)
        pyautogui.press('enter')

    def select_video(self, task: str):
        """
        Открывает нужное видео.
        :param video_number: Номер видео.
        """
        task = (task.lower().replace('{', '').replace('}', '').replace('"', '').replace("text", '')
                .replace(":", '').replace('\n', '').split(' '))

        voice_number = ' '.join([i for i in task if i in number_dict.keys()])
        playsound(choice(maked_task))
        pyautogui.click(684, 297 * number_dict[voice_number] if number_dict[voice_number] < 3 else 684,
                        297 * number_dict[voice_number] - 50)
        time.sleep(0.2)
        pyautogui.click(666, 374 * number_dict[voice_number] if number_dict[voice_number] < 3 else 666,
                        374 * number_dict[voice_number] - 50)

    def video_pause(self):
        """
        Приостанавливает видео.
        """
        playsound(choice(maked_task))
        pyautogui.click(735, 614)

    def full_ecran(self):
        """
        Переходит в полноэкранный режим.
        """
        playsound(choice(maked_task))
        pyautogui.click(1289, 902)

    def next_video(self):
        """
        Переходит к следующему видео.
        """
        playsound(choice(maked_task))
        pyautogui.moveTo(131, 1056)
        time.sleep(0.1)
        pyautogui.click()

    def make_subtiters(self):
        """
        Включает/выключает субтитры.
        """
        playsound(choice(maked_task))
        pyautogui.moveTo(1692, 1069)
        time.sleep(0.1)
        pyautogui.click()


class Google:
    def __init__(self):
        # Assuming dabl_commands is a function that returns a dictionary of commands
        self.commands_dict = dabl_commands()['commands']

class Parser:
    def joke(self):
        # Fetch jokes from a website and clean up the text
        link = requests.get('https://anekdotme.ru/')
        soup = BeautifulSoup(link.text, 'html.parser')
        select = soup.select('.anekdot_text')
        print(select)
        get = choice([i.getText().strip() for i in select])
        print(get)
        reg = re.compile("[^a-zA-Za-яА-я ^0-9:.,!?-]")
        joke = reg.sub(' ', get)

        return joke

class AddCommand(QtWidgets.QWidget, add_commands.Ui_addcomand):
    def __init__(self, commands_win):
        super(AddCommand).__init__()  # Fix: Add missing '()' for the superclass
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_command)
        self.commands_win = commands_win

    def add_command(self):
        global login
        command_name = self.lineEdit.text()
        trigers = self.lineEdit_2.text()
        action = self.comboBox.currentText()
        return_ = self.lineEdit_3.text()
        parameters = self.lineEdit_4.text()

        # Update user_commands in the database
        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            comm = dict(collect.find_one({"name": login})['user_commands'])

        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            user_commands_json = {f"{command_name}": {"trigers": trigers, "action": action, "parameters": parameters,"return": return_}}
            comm.update(user_commands_json)

            collect.update_one({"name": login}, {"$set": {"user_commands": comm}})
            self.close()
            self.commands_win.update_commands_list()


class CommanndsWin1(QtWidgets.QMainWindow, commands_win.Ui_Form):
    def __init__(self):
        global login
        try:
            super(CommanndsWin1, self).__init__()
            QtWidgets.QWidget.__init__(self)
            self.add_com_win = AddCommand(commands_win=self)

            self.setupUi(self)
            self.pushButton.clicked.connect(self.back_to_main_win)
            self.pushButton_2.pressed.connect(self.add_command)

            self.user_commands = []
            self.user_commands = [com_name for com_name in json_commands['commands'].keys()]
            with MongoClient() as cluster:
                db_con = cluster["dabl_voice"]
                collect = db_con["users_info"]
                self.json_user_commands = collect.find_one({"name": login})['user_commands'].keys()

                for name in self.json_user_commands:
                    self.user_commands.append(name)

                self.textEdit.setText("\n".join(self.user_commands))

        except Exception as e:  # Catch specific exceptions for debugging
            print(f"An error occurred: {e}")

    def add_command(self):
        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            print(login)
            self.json_user_commands = collect.find_one({"name": login})["user_commands"]
            print(self.json_user_commands)
            self.add_com_win.show()

    def update_commands_list(self):
        self.user_commands = []
        self.user_commands = [com_name for com_name in json_commands['commands'].keys()]
        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            self.json_user_commands = collect.find_one({"name": login})['user_commands'].keys()

            for name in self.json_user_commands:
                self.user_commands.append(name)

            self.textEdit.setText("\n".join(self.user_commands))

    def back_to_main_win(self):

        self.close()


class DablTasks(Youtube, Desktop, OpeningClosing, Ui_Form, threading.Thread, QtWidgets.QWidget, Parser):

    def __init__(self):
        try:
            self.commands_dict = dabl_commands()['commands']
            self.youtube = False
            self.google = False
            super(Youtube, self).__init__()
            threading.Thread.__init__(self)  # Добавьте эту строку
            QtWidgets.QWidget.__init__(self)  # И эту строку
            QtWidgets.QMainWindow.__init__(self)
            self.setupUi(self)
            self.command_win1 = CommanndsWin1()
            self.commands_window = None
            self.pushButton.clicked.connect(self.open_com_win)
            self.pushButton_2.pressed.connect(self.start_thread)
            self.pushButton_3.pressed.connect(self.off)
            self.recognize_bibliothek = None
            self.user_commands = []

            # self.Chat_GPT_mode = False
            self.YoutubeMode = False
            self.standart_commands = False
            self.work = True
        except:
            pass

    def chooseRecognizer(self):
        selected_recognize = self.comboBox.currentText()
        self.recognize_bibliothek = selected_recognize
        print(selected_recognize)

    def perform_speech_recognition(self, language):
        try:
            sr = speech_recognition.Recognizer()

            with speech_recognition.Microphone() as source:
                sr.adjust_for_ambient_noise(source=source)
                audio = sr.listen(source=source)
                query = sr.recognize_google(audio_data=audio, language=language).lower()
                self.lineEdit.setText(query)
            return query
        except:
            pass

    def open_com_win(self):
        global login, password, json_commands
        print(login, password)
        print('--' * 20)
        self.user_commands = [com_name for com_name in json_commands['commands'].keys()]
        print(self.user_commands)
        self.command_win1.show()

    # Функция для прослушивания команд и выполнения действий
    def listen(self):
        """
        Функция для прослушивания команд и выполнения действий
        :return: результат что сказал пользователь
        """
        global chunk_size, recognizer, audio_stream
        while True:
            audio_data = audio_stream.read(chunk_size, exception_on_overflow=False)
            if recognizer.AcceptWaveform(audio_data):
                result = recognizer.Result()
                result_text = " ".join([i for i in find_user_text(result) if i.isalnum()])
                print(f'Распознано: {result_text}')
                self.lineEdit.setText(result_text)

                return result.lower()

    def talk(self, text):

        tts = pyttsx3.init(debug=True)
        voices = tts.getProperty('voices')
        tts.setProperty("voice", "ru")

        # Выбираем голос "Elena" для синтеза речи
        for voice in voices:
            if voice.name == 'Aleksandr':
                tts.setProperty("voice", voice.id)

        tts.say(text)
        tts.runAndWait()

    # def Chat_GPT(self, text):
    #     messages = [{'role': 'system', 'content': 'Ты - голосовой помощник, должен быть послушным, но дерзким и немного вредный'},
    #                 {'role': 'user', 'content': 'Привет, давай поговорим о будущем.'},
    #                 {'role': 'assistent', 'content': 'Ну привет, давай поговорим'},
    #                 {'role': 'user', 'content': 'Как думаешь, что будет через 5 лет.'},
    #                 {'role': 'assistent', 'content': 'А мне откуда знать, я тебе что, гадалка?'}]
    #
    #     openai.api_key = openai_api
    #
    #     messages.append({'role': 'user', 'content': text})
    #
    #     responce = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
    #
    #     responce = responce['choices'][0]['message']['content']
    #
    #     messages.append({'role': "asistent", 'content': responce})
    #
    #     return responce
    # Функция для обработки команд пользователя
    def commands(self):
        global login, password
        """
        Функция для обработки команд пользователя
        """
        global chunk_size, recognizer, audio_stream


        while self.work:
            if self.recognize_bibliothek == 'Vosk':
                user_task = self.listen()
            else:
                user_task = self.perform_speech_recognition('ru-RU')
            count_tasks = 0

            all_commands = []
            for list_commands in self.commands_dict.values():
                print(list_commands)
                for command in list_commands:
                    all_commands.append(command.lower())

            all_user_commands = []
            with MongoClient() as cluster:
                db_con = cluster["dabl_voice"]
                collect = db_con["users_info"]
                user_data = collect.find_one({"name": login})['user_commands']

                for list_commands in user_data.values():
                    print(list_commands)
                    for command in list_commands['trigers'].split(','):
                        all_user_commands.append(command.strip().lower())

            print('--------------------------------------------')
            print(user_data)
            print(user_task)
            for task in all_commands:
                try:
                    if task in user_task:
                        self.standart_commands = True
                        print("домой")
                        if self.work:
                            print(user_task)
                            for task_name in self.commands_dict.keys():
                                for task in self.commands_dict[task_name]:
                                    task = task.lower()
                                    try:
                                        if task in user_task and task_name == 'write':
                                            count_tasks += 1
                                            if self.youtube:
                                                self.search(user_task, 943, 177)
                                            elif self.google:
                                                self.search(user_task, 796, 569)
                                        elif task in user_task and task_name == 'open_youtube':
                                            count_tasks += 1
                                            self.youtube = True
                                            self.opening_link(youtube_url, True)
                                        elif task in user_task and task_name == 'close_youtube':
                                            count_tasks += 1
                                            self.youtube = False
                                            self.closing_task('YouTube')
                                        elif task in user_task and task_name == 'open_browser':
                                            count_tasks += 1
                                            self.google = True
                                            self.opening_link(gogle_url, True)
                                        elif task in user_task and task_name == 'close_browser':
                                            count_tasks += 1
                                            self.google = False
                                            self.closing_task('Google Chrome')
                                        elif task in user_task and task_name == 'open_file_explorer':
                                            count_tasks += 1
                                            playsound(choice(opening_task))
                                            subprocess.Popen(r'explorer.exe')
                                        elif task in user_task and task_name == 'change_volume':
                                            count_tasks += 1
                                            playsound(r"C:\pythonProject10\pythonProject3\Dabl\vioce\ok_man.mp3")
                                            self.change_voice(user_task)
                                        elif task in user_task and task_name == 'change_language':
                                            count_tasks += 1
                                            self.change_language()

                                        elif task in user_task and task_name == 'pause':
                                            count_tasks += 1
                                            self.video_pause()
                                        elif task in user_task and task_name == 'open_video':
                                            count_tasks += 1
                                            self.select_video(user_task)

                                        elif task in user_task and task_name == 'full_ecran':
                                            count_tasks += 1
                                            self.full_ecran()
                                        elif task in user_task and task_name == 'next_video':
                                            count_tasks += 1
                                            self.next_video()
                                        elif task in user_task and task_name == 'make_subtiters':
                                            count_tasks += 1
                                            self.make_subtiters()
                                        elif task in user_task and task_name == 'continue_video':

                                            self.video_pause()
                                        elif task in user_task and task_name == 'you_are_good':
                                            playsound(thank_sir)


                                        elif task in user_task and task_name == 'dabl':
                                            try:
                                                playsound(yes_sir)
                                            except:
                                                playsound(r"C:\pythonProject10\pythonProject3\Dabl\vioce\yes_sir.mp3")


                                        elif task in user_task and task_name == 'tell_anikdot':
                                            joke = self.joke()
                                            self.talk(joke)
                                            continue
                                        # elif task in user_task and task_name == 'chat_gpt_mode':
                                        #     playsound(chat_gpt_mode)
                                        #     self.Chat_GPT_mode = True





                                    except:
                                        pass

                        time.sleep(1)
                except:
                    pass
            if not self.standart_commands:
                try:
                    for co in all_user_commands:
                        if co in user_task:
                            print('домой')

                            for com_name in user_data.keys():

                                for trigger in user_data[com_name]['trigers'].split(','):
                                    if trigger.strip() in user_task:

                                        if user_data[com_name]['action'] == 'open_link':
                                            count_tasks += 1
                                            self.talk(user_data[com_name]['return'])
                                            self.opening_link(user_data[com_name]['parameters'], False)
                                        elif user_data[com_name]['action'] == 'open_url':
                                            count_tasks += 1
                                            self.talk(user_data[com_name]['return'])
                                            self.opening_url(user_data[com_name]['parameters'], False)
                except:
                    pass
            self.standart_commands = False

            # if self.Chat_GPT_mode:
            #     print('Чат джипиьи запущен')
            #     gpt_answer = self.Chat_GPT(user_task)
            #     self.talk(gpt_answer)


    def off(self):
        global work
        self.work = False

        print('хелоу мир')

    def run(self):
        global work

        while self.work == True:
            self.commands()

    def start_thread(self):
        global work
        self.chooseRecognizer()
        self.work = True
        thread = threading.Thread(target=self.run, args=())
        thread.start()


class Sign_Dabl(QtWidgets.QWidget):
    def __init__(self):
        global login, password, json_commands
        QtWidgets.QWidget.__init__(self)
        self.ui = sign_dabl.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sign_in)
        self.ui.pushButton_2.clicked.connect(self.sign_up)
        self.input_login = self.ui.lineEdit.text()
        self.input_password = self.ui.lineEdit_2.text()
        login = self.input_login
        password = self.input_password

    def sign_in(self):
        global conn, cur, login, password

        self.input_login = self.ui.lineEdit.text()
        self.input_password = self.ui.lineEdit_2.text()

        login = self.input_login
        password = self.input_password

        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            if collect.count_documents({'name': self.input_login, 'password': self.input_password}) > 0:
                try:
                    playsound(welcome_dabl)
                except:
                    pass
                self.select_commands()
                self.open_second_window()


            else:
                try:
                    playsound(uncorrect_reg)
                except:
                    playsound(r'C:\pythonProject10\pythonProject3\Dabl\vioce\not_correct_reg.mp3')

    def sign_up(self):
        global login, password

        self.input_login = self.ui.lineEdit.text()
        self.input_password = self.ui.lineEdit_2.text()
        login = self.input_login
        password = self.input_password

        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]

            if collect.count_documents({"login": self.input_login}) != 0:
                playsound(another_login)
            else:
                playsound(welcome_dabl)

                self.registration(self.input_login, self.input_password)
                print('after regestration')
                self.open_second_window()
                print('hello')

    def open_second_window(self):
        self.second_window = DablTasks()
        self.second_window.show()

    def registration(self, input_login, input_password):
        with open('tasks.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            # json_data = file.read()

        user_info = {
            "name": input_login,
            "password": input_password,
            "standart_commands": json_data,
            "user_commands":
                {'openYoutube':
        {'trigers': 'открой ютуб, открой youtube, открой эту',
         'action': 'open_url', 'parameters': 'https://www.youtube.com/','return': 'Так точно!'}}
        }
        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            collect.insert_one(user_info)
            self.select_commands()

    def select_commands(self):
        global json_commands
        self.input_login = self.ui.lineEdit.text()
        self.input_password = self.ui.lineEdit_2.text()
        print(self.input_login)

        with MongoClient() as cluster:
            db_con = cluster["dabl_voice"]
            collect = db_con["users_info"]
            user_data = collect.find_one({"name": self.input_login})
            print(user_data)

            if user_data:
                standart_commands = user_data.get('standart_commands', {})
                json_commands = standart_commands

            else:
                print(f"Пользователь с логином {self.input_login} не найден.")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    wind = Sign_Dabl()
    wind.show()
    app.exec()
