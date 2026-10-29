import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Please say something...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: " + text)  
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")

# import speech_recognition as sr

# r=sr.Recognizer()

# with sr.Microphone() as source:
#     print("Please say something...")
#     audio = r.listen(source)

# try:
#     text = r.recognize_google(audio)
#     print("You said: " + text)    
# except sr.UnknownValueError:
#     print("Sorry, I could not understand the audio.")

# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Please say something...")
#     audio = r.listen(source)

# try:
#     text = r.recognize_google(audio)
#     print("You said: " + text)
# except sr.UnknownValueError:
#     print("Sorry, I could not understand the audio.")

# import customtkinter as ctk
# from PIL import Image
# import speech_recognition as sr
# import pyttsx3 
# import threading

# speaker = pyttsx3.init()
# speaker.setProperty("rate", 150)

# ctk.set_appearance_mode("light")

# window = ctk.CTk()
# window.geometry("900x600")
# window.title("Speech Recognition App")
# window.resizable(width=False, height=False)
# window.configure(fg_color="#F0F4F8")

# title_label = ctk.CTkLabel(window, text="Speech Recognition App", font=("Arial", 24, "bold"), text_color="#333333")
# title_label.pack(pady=20)

# tom_image = ctk.CTkImage(light_image=Image.open("tom.jpg"), size=(200, 200))

# tom_label = ctk.CTkLabel(window, image=tom_image, text="")
# tom_label.pack(pady=20)

# status_label = ctk.CTkLabel(window, text="Click the button and speak", font=("Arial", 16), text_color="#333333")
# status_label.pack(pady=10)

# def start_talking():
#     talk_button.configure(state="disabled")
#     status_label.configure(text="Listening... please speak!")


# window.mainloop()


import customtkinter as ctk
from PIL import Image
import speech_recognition as sr
import pyttsx3
import threading
import os

speaker = pyttsx3.init()
speaker.setProperty("rate", 150)

ctk.set_appearance_mode("light")

window = ctk.CTk()
window.geometry("900x600")
window.title("Speech Recognition App")
window.resizable(width=False, height=False)
window.configure(fg_color="#F0F4F8")

title_label = ctk.CTkLabel(window,text="Speech Recognition App",font=("Arial", 24, "bold"),text_color="#333333")
title_label.pack(pady=20)

if os.path.exists("tom image.webp"):
    tom_image = ctk.CTkImage(light_image=Image.open("tom image.webp"), size=(200, 200))
    tom_label = ctk.CTkLabel(window, image=tom_image, text="")
    tom_label.pack(pady=20)
else:
    print("Image not found! Check the file location.")

status_label = ctk.CTkLabel(window,text="Click the button and speak",font=("Arial", 16),text_color="#333333")
status_label.pack(pady=10)


def start_talking():
    talk_button.configure(state="disabled")
    status_label.configure(text="Listening... please speak!")

    def listen():
        recognizer = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            text = recognizer.recognize_google(audio)

            window.after(0, lambda: status_label.configure(text="You said: " + text))

            speaker.say(text)
            speaker.runAndWait()

        except Exception as e:window.after(0, lambda: status_label.configure(text="Error: " + str(e)[:100]))

        window.after(0, lambda: talk_button.configure(state="normal"))

    threading.Thread(target=listen, daemon=True).start()


    

def reset_button():
    status_label.configure(text="Click the button and speak")
    talk_button.configure(state="normal")

talk_button = ctk.CTkButton(window,text="Start Speaking",command=start_talking)
talk_button.pack(pady=20)

window.mainloop()




