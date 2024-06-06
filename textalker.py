# FILE: textalker.py
# AUTHOR: Ritik Pratap Singh Patel
# COMPLETION DATE: 06 June 2024
# DESCRIPTION: "Textalker": A text to Speech Converter


import tkinter as tk
from tkinter import ttk
import pyttsx3


def system_voices():

    engine = pyttsx3.init()
    return engine.getProperty("voices")


def convert_tts(text, voice_index=None, speech_rate=None):
    engine = pyttsx3.init()

    if voice_index is not None:
        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[voice_index].id)

    if speech_rate is not None:
        engine.setProperty("rate", speech_rate)

    engine.say(text)
    engine.runAndWait()


# Handle the speak button click 
def speak_button_click():
    text = text_input.get("1.0", tk.END).strip()
    voice_index = voice_combobox.current()
    speech_rate = rate_slider.get()
    convert_tts(text, voice_index=voice_index, speech_rate=speech_rate)


main_window = tk.Tk()
main_window.title("\"Textalker\": A text to Speech Converter")

#TEXT
text_label = tk.Label(main_window, text="Enter Text:")
text_label.pack(pady=5)
text_input = tk.Text(main_window, height=10, width=70)
text_input.pack(pady=5)

# Voice selection
voice_label = tk.Label(main_window, text="Select Voice:")
voice_label.pack(pady=5)
voices = system_voices()
voice_names = [voice.name for voice in voices]
voice_combobox = ttk.Combobox(main_window, values=voice_names, state="readonly")
voice_combobox.pack(pady=5)
voice_combobox.current(0)  # default to the first voice

# Speech rate adjustment
rate_label = tk.Label(main_window, text="Adjust Speech Rate:")
rate_label.pack(pady=5)
rate_slider = tk.Scale(main_window, from_=50, to_=300, orient=tk.HORIZONTAL)
rate_slider.set(150)  # default rate
rate_slider.pack(pady=5)

speak_button = tk.Button(main_window, text="Speak", command=speak_button_click)
speak_button.pack(pady=20)

main_window.mainloop()
