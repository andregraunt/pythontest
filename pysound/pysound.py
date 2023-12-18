from gtts import gTTS

from playsound import playsound

text_val = 'So much of what we do every day involves a data centre. Shopping online, streaming TV shows, reading this story - they all need data to be stored and readily available.'
#text_val = 'מה נשמה'
        
language = 'en'
#language = 'he'

obj = gTTS(text=text_val, lang=language, slow=True)


obj.save("test.mp3")
playsound("test.mp3")
