'''
This program is written by Chiiko-H.
https://github.com/Chiiko-H
'''

import tkinter as tk
import pyaudio
import wave
import subprocess
import os
import time
import datetime
import threading
import pydub


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("500x230")
        self.master.title("音声録音アプリ")
        self.master.iconbitmap(r'C:\Users\xxxxx\PycharmProjects\recTel_v2\img\favicon.ico')

        # parameter
        self.INTERVAL = 10
        self.start_time = 0
        self.start_flag = False
        self.after_id = 0
        self.REC_DIR = "C:\\rec"

        self.rec_data = []
        self.rec_status = False

        # initialize
        def initialize():
            recTimer.configure(text='00:00')
            fileName.configure(text='')
            audioCheck()

        # audio
        def audioCheck():
            #print('audio check')
            py = pyaudio.PyAudio()
            audioList = py.get_device_info_by_index(1)
            # print(audioList['name'])
            if 'マイク' in audioList['name']:
                self.value = "マイク接続済み"
                recBtn["state"] = tk.NORMAL
            else:
                self.value = "マイクが接続していません\n接続してから起動してください"
                recBtn["state"] = tk.DISABLED

        # recording
        def audiostart():
            # print('audio start')
            audio = pyaudio.PyAudio()
            stream = audio.open(format=pyaudio.paInt16,
                                rate=44100,
                                channels=1,
                                input_device_index=1,
                                input=True,
                                frames_per_buffer=1024)
            return audio, stream

        def audiostop(audio, stream):
            # print('audio stop')
            stream.stop_stream()
            stream.close()
            audio.terminate()

        def read_plot_data(stream):
            data = stream.read(1024)
            return data

        def rec_exec(data):
            # print('save')
            rec_data = data
            dt_now = datetime.datetime.now()
            filename = dt_now.strftime('%Y%m%d_%H%M%S')
            file_path = self.REC_DIR + "\\" + filename + ".wav"
            # 録音データをファイルに保存
            wave_f = wave.open(file_path, 'wb')
            wave_f.setnchannels(1)
            wave_f.setsampwidth(2)
            wave_f.setframerate(44100)
            wave_f.writeframes(b''.join(rec_data))
            wave_f.close()
            # wav -> mp3
            sound = pydub.AudioSegment.from_wav(file_path)
            sound.export(self.REC_DIR + "\\" + filename + ".mp3", format="mp3")
            mp3_filename = filename + ".mp3"
            fileName.configure(text=mp3_filename)
            # delete wav file
            os.remove(file_path)

        def recording():
            # print('recording....')
            (audio, stream) = audiostart()
            rec_data = []
            # print("Start")
            while True:
                try:
                    data = read_plot_data(stream)
                    rec_data.append(data)
                    if (self.rec_status == False):
                        # print('try stop')
                        break
                except KeyboardInterrupt:
                    # print("KeyboardInterrupt")
                    break
            audiostop(audio, stream)
            rec_exec(rec_data)

        # action
        def openExplorer():
            # print('open explorer')
            if not os.path.exists(self.REC_DIR):
                os.makedirs(self.REC_DIR)
            subprocess.Popen(['explorer', self.REC_DIR], shell=True)

        def convert(sec):
            minits = sec // 60
            second = sec % 60
            milli_sec = (second - int(second)) * 1000
            hour = minits // 60
            min = minits % 60
            return f"{'{0:02}'.format(int(min))}:{'{0:02}'.format(int(second))}"

        def update_time():
            self.after_id = self.master.after(self.INTERVAL, update_time)
            now_time = time.time()
            elapsed_time = now_time - self.start_time
            elapsed_time_str = convert(elapsed_time)
            recTimer.config(text=elapsed_time_str)

        def recStart():
            # print('rec start')
            self.rec_status = True
            recBtn.configure(text="■", command=recStop)
            openFolder["state"] = tk.DISABLED
            if not self.start_flag:
                initialize()
                self.start_flag = True
                self.start_time = time.time()
                self.after_id = self.master.after(self.INTERVAL, update_time)

            thread1 = threading.Thread(target=recording)
            thread1.start()

        def recStop():
            # print('rec stop')
            self.rec_status = False
            openFolder["state"] = tk.NORMAL
            recBtn.configure(text="●", command=recStart)
            if self.start_flag:
                self.master.after_cancel(self.after_id)
                self.start_flag = False

        # button
        recBtn = tk.Button(self.master, text="●", font=("", 18), width=5, height=2, fg='red', command=recStart)
        openFolder = tk.Button(self.master, text='開く', font=("", 16), width=10, height=2, command=openExplorer)
        #self.img = tk.PhotoImage(file="./img/renew.png")
        #renewBtn = tk.Button(self.master, image=self.img, command=initialize, compound="top")

        # label
        audioCheck()
        self.micStatus = tk.Label(self.master, borderwidth=2, text=self.value, relief="ridge", font=("", 16), width=25,
                                  height=2)
        recTimer = tk.Label(borderwidth=2, relief="ridge", text="00:00", font=("", 16), width=10, height=2)
        fileName = tk.Label(font=("", 10), width=18, height=2)

        # arrange
        recBtn.place(x=10, y=120)#
        openFolder.place(x=350, y=120)
        # renewBtn.place(x=300, y=25)
        self.micStatus.place(x=10, y=20)
        recTimer.place(x=350, y=20)
        fileName.place(x=150, y=120)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
