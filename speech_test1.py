#Instalar librerías para procesamiento de audio y de reconocimiento de voz
#pip install pydub
#pip install SpeechRecognition

#Es necesario instalar los FFmpeg para la manipulación del audio

from os import path
import speech_recognition as sr
from pydub import AudioSegment
import os
import math

#Se especifica el path del archivo de audio
audio_file_path = 'coronavirus.mp3'

#Se convierte el audio de formato mp3 a flac
#También funciona con audios en formato wma, ogg, flv, aiff
song = AudioSegment.from_file(audio_file_path,"mp3")
duration = len(song)
segments = math.ceil(duration/(30*1000))
print(segments)
for i in range(0, segments):
	min_a = 30000 * (i)
	min_b = 30000 + min_a	
	audio = song[min_a:min_b]
	audio.export("speech.flac", format="flac")
	audio_file = "speech.flac"

	#Se instancia la librería de reconocimiento de voz
	r = sr.Recognizer()
	with sr.AudioFile(audio_file) as source:
	    audio = r.record(source)

	#Se convierte al audio a texto y se imprime en consola
	try:
	    print(r.recognize_google(audio, language = "es-CO"))
	except sr.UnknownValueError:
	    #print("Could not understand audio")
	    print('---')
	except sr.RequestError as e:
	    #print("Error; {0}".format(e))
	    print('---')

	#Se elimina el archivo .flac que se generó durante la conversión
	os.remove("speech.flac")	