import pyttsx3
# Método para iniciar o sintetizador de voz. Retorna objeto com as configuraões iniciais do sintetizador.
def IniciarSintetizadorTTS(numeroDaVoz = 4):
    Robo = pyttsx3.init()
    voices = Robo.getProperty('voices')
    Robo.setProperty('voice', voices[numeroDaVoz].id) 
    return Robo
