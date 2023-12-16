import time
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
from PyQt5.QtCore import pyqtSignal
from dablwindow import Ui_Form
import sqlite3
import sign_dabl


tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty("voice", "ru")

# Выбираем голос "Elena" для синтеза речи
for voice in voices:
    if voice.name == 'Elena':
        tts.setProperty("voice", voice.id)


model_vosk = r"C:\pythonProject10\pythonProject3\vosk_model_small"

model = vosk.Model(model_vosk)

conn = sqlite3.connect('dabl.db')
cur = conn.cursor()

sample_rate = 16000
chunk_size = 1024

audio = pyaudio.PyAudio()
audio_stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

recognizer = vosk.KaldiRecognizer(model, sample_rate)

work = True
mir = False



# Функция для загрузки задач из файла tasks.json
def dabl_commands() -> dict:
    """
    Загружаем задачи из файла tasks.json
    :return: Словарь с задачами
    """
    with open('tasks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def find_user_text(text: str) -> list:
    text = text.lower().replace('{', '').replace('}', '').replace('"', '').replace("text", '').replace(":", '').replace('\n', '').split(' ')
    return text


def make_db():
    global conn, cur

    cur.execute('''CREATE TABLE IF NOT EXISTS dabl (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_login TEXT,
        password TEXT,
        plan_day TEXT,
        open_link_command TEXT,
        open_path_command TEXT
        )''')

make_db()

class Desktop:
    # Функция для смены языка клавишей "Alt+Shift"
    def change_language(self):
        """
        Смена языка клавишей "Alt+Shift"
        """
        playsound(choice(maked_task))
        pyautogui.hotkey('alt', 'shift')

    # Функция для изменения громкости звука
    def change_voice(self, task: str):
        """
        Изменение громкости звука
        :param task: Команда с уровнем громкости
        """
        commands = dabl_commands()['commands']

        # Обработка текстовой команды, извлечение числа (громкости)
        task = (find_user_text(task))
        print(task)
        voice_number = ' '.join([i for i in task if i in number_dict.keys()])

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        print('--------------')
        print(voice_number)
        # Установка громкости
        volume.SetMasterVolumeLevelScalar(float(f'0.{number_dict[voice_number]}'), None)

class Music:
    def open_music(self, task: str):
        text = find_user_text(task)
        song = [i for i in task if i not in ['включи песню', 'включи музыку']]

        print('-' * 100)
        print(song)


class OpeningClosing:
    # Функции для открытия и закрытия различных приложений
    def opening_browser_youtube(self, by_url: str):
        """
        Открытие браузера и переход на YouTube
        :param by_url: URL YouTube
        """
        playsound(choice(opening_task))
        webbrowser.open(by_url)

    def opening_task(self, url):
        """
        Открытие задачи
        :param url: Путь к задаче
        """
        playsound(choice(opening_task))
        os.system(url)

    def closing_task(self, name):
        """
        Закрытие приложения по имени
        :param name: Имя приложения
        """
        playsound(choice(maked_task))
        windows = gw.getWindowsWithTitle(name)
        window = windows[0]
        window.close()

class Youtube:
    def __init__(self):
        self.commands_dict = dabl_commands()['commands']

    # Функция для поиска текста и ввода его в поле поиска
    def search(self, task: str, x, y):
        """
        Поиск текста и ввод в поле поиска
        :param task: Текст для поиска
        :param x: Координата x
        :param y: Координата y
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
        Открываем нужное видео
        :param video_number:
        """
        task = (task.lower().replace('{', '').replace('}', '').replace('"', '').replace("text", '')
                .replace(":", '').replace('\n', '').split(' '))

        voice_number = ' '.join([i for i in task if i in number_dict.keys()])
        playsound(choice(maked_task))
        pyautogui.click(684, 297 * number_dict[voice_number] if number_dict[voice_number] < 3 else 684, 297 * number_dict[voice_number] - 50)
        time.sleep(0.2)
        pyautogui.click(666, 374 * number_dict[voice_number] if number_dict[voice_number] < 3 else 666, 374 * number_dict[voice_number] - 50)
    def video_pause(self):
        """
        Пауза видео
        """
        playsound(choice(maked_task))
        pyautogui.click(735, 614)

    def full_ecran(self):
        """
        Переход на полный экран
        """
        playsound(choice(maked_task))
        pyautogui.click(1289, 902)

    def next_video(self):
        """
        Переход на следующий видео
        """
        playsound(choice(maked_task))
        pyautogui.moveTo(131, 1056)
        time.sleep(0.1)
        pyautogui.click()

    def make_subtiters(self):
        """
        Включаем, выключаем субтитры
        """
        playsound(choice(maked_task))
        pyautogui.moveTo(1692, 1069)
        time.sleep(0.1)
        pyautogui.click()


class Google:
    def __init__(self):
        self.commands_dict = dabl_commands()['commands']


class DablTasks(Youtube, Desktop, OpeningClosing, Ui_Form, threading.Thread, QtWidgets.QWidget):

    def __init__(self):
        try:
            self.commands_dict = dabl_commands()['commands']
            self.youtube = False
            self.google = False
            super(Youtube, self).__init__()
            threading.Thread.__init__(self)  # Добавьте эту строку
            QtWidgets.QWidget.__init__(self)  # И эту строку
            self.setupUi(self)
            self.pushButton_2.pressed.connect(self.start_thread)
            self.pushButton_3.pressed.connect(self.off)
            self.work = True
        except:
            pass


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

    # Функция для обработки команд пользователя
    def commands(self):
        """
        Функция для обработки команд пользователя
        """
        global chunk_size, recognizer, audio_stream

        global chunk_size, recognizer, audio_stream

        while self.work:
            user_task = self.listen()
            count_tasks = 0

            if self.work:
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
                                self.opening_browser_youtube(youtube_url)
                            elif task in user_task and task_name == 'close_youtube':
                                count_tasks += 1
                                self.youtube = False
                                self.closing_task('YouTube')
                            elif task in user_task and task_name == 'open_browser':
                                count_tasks += 1
                                self.google = True
                                self.opening_browser_youtube(gogle_url)
                            elif task in user_task and task_name == 'close_browser':
                                count_tasks += 1
                                self.google = False
                                self.closing_task('Google Chrome')
                            elif task in user_task and task_name == 'open_file_explorer':
                                count_tasks += 1
                                playsound(choice(opening_task))
                                subprocess.Popen(r'explorer.exe')
                            elif task in user_task and task_name == 'close_file_explorer':
                                count_tasks += 1
                                self.closing_task('Проводник')
                            elif task in user_task and task_name == 'change_volume':
                                count_tasks += 1
                                playsound(r"C:\pythonProject10\pythonProject3\Dabl\vioce\ok_man.mp3")
                                self.change_voice(user_task)
                            elif task in user_task and task_name == 'change_language':
                                count_tasks += 1
                                self.change_language()
                            elif task in user_task and task_name == 'open_discord':
                                count_tasks += 1
                                self.opening_task(discord_opening)
                            elif task in user_task and task_name == 'close_discord':
                                count_tasks += 1
                                self.closing_task('Discord')
                            elif task in user_task and task_name == 'open_spotify':
                                count_tasks += 1
                                self.opening_task(spotify_opening)
                            elif task in user_task and task_name == 'close_spotify':
                                count_tasks += 1
                                self.closing_task('Spotify')
                            elif task in user_task and task_name == 'open_obs':
                                count_tasks += 1
                                self.opening_task(obs_opening)
                            elif task in user_task and task_name == 'close_obs':
                                count_tasks += 1
                                self.closing_task('OBS Studio (64bit)')
                            elif task in user_task and task_name == 'open_visual_studio':
                                count_tasks += 1
                                self.opening_task(vs_code_opening)
                            elif task in user_task and task_name == 'close_visual_studio':
                                count_tasks += 1
                                self.closing_task('Visual Studio Code')
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
                                count_tasks += 1
                                self.video_pause()
                            elif task in user_task and task_name == 'you_are_good':
                                playsound(thank_sir)

                            elif task in user_task and task_name == 'open_song':
                                pass
                            elif task in user_task and task_name == 'dabl':
                                try:
                                    playsound(yes_sir)
                                except:
                                    playsound(r"C:\pythonProject10\pythonProject3\Dabl\vioce\yes_sir.mp3")
                            elif task in user_task and task_name == 'i_at_home':
                                playsound(come_back)
                                webbrowser.open('https://youtu.be/G2uGZ9Bt8JU?si=PpHgMgl2dHuBew76')




                        except:
                            pass


            time.sleep(1)














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
        self.work = True
        thread = threading.Thread(target=self.run, args=())
        thread.start()


class Sign_Dabl(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = sign_dabl.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sign_in)
        self.ui.pushButton_2.clicked.connect(self.sign_up)
    def sign_in(self):
        global conn, cur
        input_login = self.ui.lineEdit.text()
        input_password = self.ui.lineEdit_2.text()
        cur.execute(f'''SELECT user_login, user_password FROM dabl''')
        print(cur.fetchall())

    def sign_up(self):
        global conn, cur
        input_login = self.ui.lineEdit.text()
        input_password = self.ui.lineEdit_2.text()

        cur.execute('''SELECT user_login FROM dabl''')

        if input_login in [item[0] for item in cur.fetchall()]:
            playsound(another_login)
        else:
            playsound(welcome_dabl)

            cur.execute(f'''INSERT INTO dabl (user_login, user_password) VALUES (?,?)''', (input_login, input_password))



            # Отобразить окно DablTasks
            app = QtWidgets.QApplication([])
            window = DablTasks()
            window.show()
            app.exec()







if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    wind = DablTasks()
    wind.show()
    app.exec()
