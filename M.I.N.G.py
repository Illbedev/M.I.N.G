# import thư viện
import pyttsx3
from datetime import date, datetime
import speech_recognition
import webbrowser

# khởi tạo các biến
running = True
bot_mouth =  pyttsx3.init()
bot_ear = speech_recognition.Recognizer()


voice = bot_mouth.getProperty('voices')
bot_mouth.setProperty('voice',voice[1].id)

def speak(audio):
	print('F.R.I.D.A.Y: ' + audio)
	bot_brain = audio
	bot_mouth.say(bot_brain)
	bot_mouth.runAndWait()

def time():
	Time = datetime.now().strftime('%I: %M %p')
	speak(Time)

def welcome():
	hour = datetime.now().hour
	if hour >= 6 and hour <12:
		speak('good morning Minh!')
	elif hour >= 12 and hour <19:
		speak('good afternoon Minh!')
	elif hour >= 19 and hour <24:
		speak('good night Minh!')  
	speak('how can i help you')
def today():
	today = date.today()
	a = today.strftime("%B %d, %Y")
	speak(a)
def lowercase(you):
	a = you.lower()
def youtube():
	with speech_recognition.Microphone() as mic:
		audio = bot_ear.listen(mic)
		you = bot_ear.recognize_google(audio)
		lowercase(you)
		print('You: ' + you)
		webbrowser.open('https://www.youtube.com/results?search_query={0}'.format(you))
# def bing():
# 	with speech_recognition.Microphone() as mic:
# 		audio = bot_ear.listen(mic)
# 		you = bot_ear.recognize_google(audio)
# 	lowercase(you)
# 	print('You: ' + you)
# 	webbrowser.open('https://www.bing.com/search?q={0}'.format(you))

	

welcome()

while running:
	with speech_recognition.Microphone() as mic:
		audio = bot_ear.listen(mic)
	try:
		you = bot_ear.recognize_google(audio)
	except:
		you = ''
	
	print('....')
	print('You: ' + you)
	lowercase(you)
	if you == '':
		speak('i cant hear you')

	elif 'time' in you:
		time()

	elif 'president' and 'America' in you:
		speak('Joe Biden')

	elif 'today' in you:
		today()

	elif 'bye' in you:
		speak('good bye')
		running = False

	elif 'Youtube' or 'youtube' in you:
		speak('what do you want to search??')
		youtube()

	else:
		speak('i cant run it for but i will train')



