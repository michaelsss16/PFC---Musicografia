import pyttsx3
def IniciarSintetizadorTTS():
    Robo = pyttsx3.init()
    voices = Robo.getProperty('voices')
    Robo.setProperty('voice', voices[4].id) 
    return Robo
