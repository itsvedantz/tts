import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import speech_recognition as sr
import subprocess
from gtts import gTTS
from googletrans import Translator
from tkinter import ttk
from tkinter import messagebox
import threading
import os
import textblob as textblob

class trans:
    def __init__(self, root):
        self.root = root
        self.root.title('Translation')
        self.root.geometry("1600x900+0+0")
        self.root.configure(bg="steelblue1")

        self.languages = {'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz', 'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian', 'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'ps': 'Pashto', 'fa': 'Persian', 'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan', 'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu'}
        
        self.create_widgets()
        self.label_change()
        
    def create_widgets(self):
        self.label1 = tk.Label(self.root, text='!!! SPEECH TO TEXT !!!', font=("Roboto 14", 15), width=20, bg='white smoke')
        self.label1.place(x=670, y=50)

        self.text1 = tk.Text(self.root, font=100, height=10, width=48, bg='gainsboro', bd=5)
        self.text1.place(x=200, y=320)

        self.recordbutton = tk.Button(self.root, text='RECORD', fg='white', width=15, bg='black', font="Roboto 14", height=1, command=self.record_action)
        self.recordbutton.place(x=300, y=580)

        self.text_translate = tk.Text(self.root, font=20, height=10, width=48, bg='gainsboro', bd=5)
        self.text_translate.place(x=800, y=320)

        self.combo = ttk.Combobox(self.root, values=list(self.languages.values()), font="Roboto 14")
        self.combo.place(x=920, y=220)
        self.combo.set("SELECT LANGUAGE")

        self.talkbutton = tk.Button(self.root, text="SPEAK", font="Roboto 15 bold", width=15, bg="red", fg="white", command=self.talk)
        self.talkbutton.place(x=920, y=630)

        self.label1 = tk.Label(self.root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=tk.GROOVE)
        self.label1.place(x=800, y=260)

        self.translate_btn = tk.Button(self.root, text="TRANSLATE", font="Roboto 15 bold", width=15, bg="red", fg="white", command=self.translate_now)
        self.translate_btn.place(x=920, y=580)

        self.logout_btn = tk.Button(self.root, text="LOG OUT", font="Roboto 15 bold", width=15, bg="red", fg="white", command=self.logout)
        self.logout_btn.place(x=1330, y=10)
        
    def speech(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Speak now")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        except Exception as e:
            print("Unexpected error occurred:", str(e))

    def record_action(self):
        
        threading.Thread(target=self.record_audio).start()

    def record_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak now")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            self.text1.insert(tk.END, text)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        except Exception as e:
            print("Unexpected error occurred:", str(e))

    def talk(self):
        try:
            text = self.text_translate.get(1.0, tk.END)
            language = "hi"  
            if text:
                tts = gTTS(text=text, lang=language, slow=False)
                tts.save("translated_audio.wav")
                showinfo("Success", "Translated text converted to audio successfully!")

             
                result = messagebox.askyesno("Audio Options", "Do You Want To Play The Audio?")
                if result:
                    
                    subprocess.Popen(["start", "translated_audio.wav"], shell=True)
        except Exception as e:
            showerror("Error", str(e))

    def translate_now(self):
        try:
            dest_lang = list(self.languages.keys())[list(self.languages.values()).index(self.combo.get())]
            text_ = self.text1.get(1.0, tk.END)
            if text_:
                translator = Translator()
                result = translator.translate(text_, dest=dest_lang)
                self.text_translate.delete(1.0, tk.END)
                self.text_translate.insert(tk.END, result.text)
        except Exception as e:
            showerror("Error", str(e))

    def label_change(self):
        c = self.combo.get()
        self.label1.configure(text=c)
        self.root.after(1000, self.label_change)

    def logout(self):
        self.root.destroy()
        import log

if __name__ == "__main__":
    root = tk.Tk()
    app = trans(root)
    root.mainloop()