
import pyttsx 
def cb(name):
	print(name)
engine = pyttsx.init() 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
engine.connect('started-utterance', cb)

while True:
	g =  raw_input()
	if(g=='a'):
		print g
		engine.say('Welcome')
		engine.runAndWait()
	if(g=='b'):
		print g
		engine.say('Semua')
		engine.runAndWait()
engine.say('Halo')
engine.runAndWait()
