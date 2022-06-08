'''
This program is written by Chiiko-H.
https://github.com/Chiiko-H
'''

import tkinter as tk

import ffmpeg
import pyaudio
import wave
import subprocess
import os
import time
import datetime
import threading
#import pydub


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("500x230")
        self.master.title("音声録音アプリ")
        data = '''R0lGODlhAAEAAfQAAAAAAN1VVd5UVN9UVN5VVd9VVdxWVt1WVt1XV95WVt9WVt5X
                V99XV95YWOBVVeFVVeBWVuFWVuBXV+FXV+JWVuBYWAAAAAAAAAAAAAAAAAAAAAAA
                AAAAAAAAAAAAAAAAACH5BAEAAAAAIf8LSW1hZ2VNYWdpY2sNZ2FtbWE9MC40NTQ1
                NQAh/wtYTVAgRGF0YVhNUDw/eHBhY2tldCBiZWdpbj0n77u/JyBpZD0nVzVNME1w
                Q2VoaUh6cmVTek5UY3prYzlkJz8+Cjx4OnhtcG1ldGEgeG1sbnM6eD0nYWRvYmU6
                bnM6bWV0YS8nIHg6eG1wdGs9J0ltYWdlOjpFeGlmVG9vbCAxMi4xNic+CjxyZGY6
                UkRGIHhtbG5zOnJkZj0naHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYt
                c3ludGF4LW5zIyc+CgogPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9JycKICB4
                bWxuczp0aWZmPSdodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyc+CiAgPHRp
                ZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KIDwvcmRmOkRlc2Ny
                aXB0aW9uPgo8L3JkZjpSREY+CjwveDp4bXBtZXRhPgogICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAog
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
                ICAgICAgIAo8P3hwYWNrZXQgZW5kPSd3Jz8+Af/+/fz7+vn49/b19PPy8fDv7u3s
                6+rp6Ofm5eTj4uHg397d3Nva2djX1tXU09LR0M/OzczLysnIx8bFxMPCwcC/vr28
                u7q5uLe2tbSzsrGwr66trKuqqainpqWko6KhoJ+enZybmpmYl5aVlJOSkZCPjo2M
                i4qJiIeGhYSDgoGAf359fHt6eXh3dnV0c3JxcG9ubWxramloZ2ZlZGNiYWBfXl1c
                W1pZWFdWVVRTUlFQT05NTEtKSUhHRkVEQ0JBQD8+PTw7Ojk4NzY1NDMyMTAvLi0s
                KyopKCcmJSQjIiEgHx4dHBsaGRgXFhUUExIREA8ODQwLCgkIBwYFBAMCAQAALAAA
                AAAAAQABAAX+ICCOZGmeaKqubOu6EKQ4ca3IEH1Db+//wKBwSCwaUzGFcqlMMp+y
                W5NZO1qv2Kx2i6xEl86neEwWOyGNGHfNbruPjbJ8Tpd/K++8ft/e1f+AgU98hIWG
                LGaCiot1h46PbzaMk5R2apCYmUOVnJ10l5qhoiaepaZkUaOqmaetrmKrsXyvtLVL
                srhctru1Dbm/RrzCtsDFPsPIxMbLKMnOyszMz9PQ0bnU2NXWqlLZ3q3b3N/jr+Gs
                5OiuPOaH6e6u7ITv8/DxkfT4pTL2a/n+pr74Zen2r2AlgVYIGlzIaB/CTQwjcnoY
                RKHEi4Io+viCsWMghxpVeBw5KSQSkij+FZkklbJloJUjLLqcSQamTJo4wazTmLPn
                HJ4+g9ZEKLToGH5Gk0JREE+p01vmnkplum3qVGtWrUrLOnXnrzBcnwLjGPap11Vl
                y8pKWxaPOLZcQYaCm3bUTbpiNaXBWxfTXb5S/QJmC+nv4LyGDuNtp5jtWT2NF/Mh
                G1ntHnyUKwu7TO9EZs313MRJJ/cE6F2Pt7x7cbqWm9U9Wr9KjcUdENmht4DFBurH
                aNyldH121hvIcOCLVKMr/QN58IHziDj3lOU4NebHph+8Yt2bdO2UrpADsFsJke7g
                hwYbRyIzkQrpk6/PdrbM9/iAaGf3zhJKQCHo4QfVEAG61ox6FQn++Md92Yhkhn4w
                KNiIEN8gkgiDEiK4X4OIkIUGhhnCAgR8/LVAGYQmhjgGiilU2IN7EKk4SHMusqYh
                jTIygSOHsXn4X4I5mvcie8aZEWOQLJIwXhCU/bijiti1SORtKx4po41T3uYjgEHe
                4MI4xTXnIVVPQvnlN1FudJSYXaa4JIgDYolkh29Kd+KGMobZH5rcGSlnkCsUuFmf
                UPyZJ4SC8lLdmit0SYWDy0EnopSOxrknmJJOalqllrZHmpNH3HQgp52KEJ0WqFxK
                Kgq/kZMkkIXGROqMJSQ6DBt3AjCrn0p2toatlaqKDhu7AiIspsQCC2h7yirqRrNm
                jlDesM/+FluGV9A6S6y1cniKTx/ZhthrPslya5+s5PZj7rmm+rPtuozq6s+rQbQK
                74AGqXtvrPnqu28T7f5Db5H/QrWQvwUHXBDC+4oQLjL9PKygwv/gWjBVC6V5hMT4
                yctQH/+Sx/GtDK87MsklW4uGRAMzeXFEr8Fr78fvvtwvG3uZe3IyMevc0T3Wkvhz
                zzbP+0bRAueBdMVHL/2t0k77CnTUtkFNdTqcXU2t1TnGsfM0EAyQtdY1ci2uxynN
                ciXaKLU8X4YUoyTP2TNpzMXXfc1Mkttvd8x2S4VI6HBOgQuD96nTyj23gce2jS5O
                heANIU5e9WS3LuC0QNO4hCf23Jn+gD/eeeET4TmStz4xFh6Vig8ulOryweoRs0XB
                /hGcEWFrFN/ixS77RSUo5QgjuN8s+uvDC8r78QfX6lRhK35GRM40B/889PjCyGX1
                zl+/iva/u2va4U9zAz7BSXtGfvmqnP/D+vpQilj78bKeLgrwsz+K+6bD1kz+UqOf
                ptB3qlFpBS038oHe6rQpqyyPaLQKX5b+lxW3vGWAZfKGnrqXlQeCrH4ZpI/mwuLB
                NvDvBYmbRoQsg0AMxsZVoGOhXRIYQw0aiitoOeEIy2YhuMQiVyFMxuU4R5jvgXCH
                InyhZPa3lCDyTE10GWLkxGDBLwGwW06MywyPKD9qSLCIcwH+IguumCr7DYaJLiQF
                GWmIxDOKQoz4W2MaazgYUD1iTIEqkcsaU8JMNUE/PDRjYzSxoioy7xl94yMrPFQf
                GyYyMueAggUNg7Ii4EYwUOABA88DHEzI8SWEkk0fi/DJCfXOOcMr4CmBI0XlYA1V
                pazbKLOISN3EZ5Z01COqBITLLgbSj/jpJREn6MoMpWGVm9zCAoO5wRsSE3OzyuXW
                muaz5ukhlmTTkdqy6cXFcdMZh1jmN2mRvHEOKpXm1Ibn0sm4R7DzFXa03Ts7scV5
                lk4U9qTOBfPpu3ryMz/X+Ccor4HNYgkTVwXlVCsJKVB2LaOhXAQGRLUZjomSqaIN
                XSjCLgT6EH4C5Z0mAelKEjodmMSNagf9YTZNaj2qxdOkJOXjRVkavJi6kaa+bBhO
                x7gvjbJUpzt1JqdeGtQW2dQsMy2qUNemVAo5qqmP5GVKd6oiqMLSb1a9KniyWrNO
                chWCoPnq2CApVm/etKykowtR0QoZH7J1LlJJxVtbWBQZrHWumTiqOqaK11+lkCFV
                6Gs49KqIZgoWK+JcDl8P60lUPJOxIT2DLca0A8iWtTxgsQ4jDWvZvurABkmogWgN
                2VkAhAAAOw==      
                '''
        self.master.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(data=data))

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
            #sound = pydub.AudioSegment.from_wav(file_path)
            #sound.export(self.REC_DIR + "\\" + filename + ".mp3", format="mp3")

            stream = ffmpeg.input(file_path)
            stream = ffmpeg.output(stream, self.REC_DIR + "\\" + filename + ".mp3")
            ffmpeg.run(stream)

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
