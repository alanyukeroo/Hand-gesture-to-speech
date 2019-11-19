import pyttsx

def say(s):
	engine = pyttsx.init()
	engine.say(s)
	a = engine.runAndWait()
	engine.runAndWait()
	#engine.stop()

#b = raw_input()

while True:
	b = raw_input()
	if(b=='a'):
		say('Hallo')
	if(b=='b'):
		say('Yes')
	#engine.stop()	
