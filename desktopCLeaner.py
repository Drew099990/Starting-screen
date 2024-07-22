import os
import shutil
import time
from tkinter import *
from tkinter.ttk import *

destination = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\0"
play_ground = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop"
main = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\FileManager"
audio = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\FileManager\\audios"
video = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\FileManager\\videos"
document = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\FileManager\\documents"
image = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\FileManager\\images"
other = "C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\FileManager\\others"

os.chdir(play_ground)
files = os.listdir()

os.makedirs(audio, exist_ok=True)
os.makedirs(video, exist_ok=True)
os.makedirs(document, exist_ok=True)
os.makedirs(image, exist_ok=True)
os.makedirs(other, exist_ok=True)

FIXED = ['#', '0', 'drew', 'exxam prep', 'FileManager', 'goals for the holidays', 'music', 'study', 'study music', 'two categories of algorithms.pdf']

def organizer():
    for file in files:
        path = os.path.join(play_ground, file)
        if os.path.isfile(path):
            if file not in FIXED:
                if path.endswith((".mp3", ".wav")):
                    shutil.move(path, audio)
                elif path.endswith((".mp4", ".mov", ".avi")):
                    shutil.move(path, video)
                elif path.endswith((".pdf", ".txt", ".py", ".java", ".bat")):
                    shutil.move(path, document)
                elif path.endswith((".png", ".jpg")):
                    shutil.move(path, image)
                else:
                    shutil.move(path, other)

def progressor():
    number = 0
    total = len(files)
    for _ in files:
        number += 1
        progress["value"] += (100 / total)
        time.sleep(0.2)
        label.config(text=f"{number}/{total}")
        window.update()
    window.destroy()

window = Tk()
window.title("File Organizer")
window.geometry("400x70")

progress = Progressbar(window, orient="horizontal", length=300)
progress.pack()

label = Label(window, font=("ink free", 16, "italic"), text="")
label.pack()

label2 = Label(window, font=("ink free", 16, "italic"), text="Organizing files...")
label2.pack()

organizer()
progressor()

window.mainloop()