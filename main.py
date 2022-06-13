import os #importing os library for the api key
import telebot #importing the main pyTelebotAPI
from datetime import datetime, time, date #importin datetime for the time and date functionality in the bot
import pytz #importing pytz library for the changing of timezone
from keep_alive import keep_alive #importing keep_alive file and keep_alive function for running the bot continously
import requests #imorting request for the weatherAPI request


#here goes our telegram bot api key
my_secret = os.environ['key']
bot = telebot.TeleBot(my_secret)

#here goes our weather bot api
my_secret = os.environ['weatherapi']
base_url = 'https://api.openweathermap.org/data/2.5/weather?q=Ropar&appid=d850f7f52bf19300a9eb4b0aa6b80f0d'

#we are defining a function to take commands it will begin by typing start
@bot.message_handler(commands=['start']) #defining a function to start the conversation.
def send_welcome(message): #function for the reply of start command
  '''This function will reply to the very first command of the user that is start command'''
  bot.reply_to(message, "Hi my Name is Dragon, I am a general conversation bot and currently I can tell you Date, Time, Weather and all the social media links.")
  
#checking input message
def input_message(message):  
  '''This function will take the user input message and will check wheather the message is valid or not'''
  request = message.text.split()  #Splitting the input message

  for i in range(len(request)):    #Making the message in lower case
    request[i] = request[i].lower()

  if len(request) < 1:      # checking for valid message
    return False #if message is valid then return false
  else:
    return True #if message is not valid then return true

def weather_message(message): #defining a weather function for checking the weather keyword in message
  '''This function will check for the message which contains the weather keyword in it and if the weather keyword will come with a city name then it will return true else it will return false'''
  request = message.text.split()  #Splitting the input message
  
  for i in range(len(request)):    #Making the message in lower case
    request[i] = request[i].lower()

  if len(request)<2 and request[0] != "weather":
    return False #if the first keyword is not weather and len of message is less than 2 then return false
  else:
    return True #else return True

 
#Simple response start here
@bot.message_handler(func = input_message)
def simple_responses(message): #defining a function for simple messages or general messages
  '''This function will reply to all the message which contains simple messages'''
  request = message.text.split()   #Splitting the input message
  
  for i in range(len(request)):    #Making the message in lower case
    request[i] = request[i].lower()
    #converting words in input sentence into lower case,so as to avoid upper case errors.
  
  if "time" in request or "date" in request: #if the message contains date or time keyword then sending the realtime date and time data
    IST = pytz.timezone('Asia/Kolkata')  #using pytz api for changing the timezone to india
    now = datetime.now(IST)
    current_time = "Date =" + now.strftime("%d/%m/%Y") + "\n" + "Time ="+ now.strftime("%I:%M:%S")
    bot.reply_to(message, current_time)
    #piece of code is written to know the time.
  #piece of codes are written as they reply for the most general questions asked in a chat box.
    
  elif "hello" in request or "hi" in request or "hi" in request or "greet" in request:
    greet = "Hey! hi, How are you doing?" #message for hello
    bot.reply_to(message, greet)

  elif "morning" in request:
    greet = "Hey! good morning, How are you doing?" #message for good morning
    bot.reply_to(message, greet)
 
  elif "afternoon" in request:
    greet = "Hey! good afternoon, How are you doing?" #message for good afternoon
    bot.reply_to(message, greet)

  elif "evening" in request:
    greet = "Hey! good evening, How are you doing?"  #message for good evening
    bot.reply_to(message, greet)

  elif "night" in request:
    greet = "Sleep well and dream big,\ntomorrow is the start of something great.\n\nGood night!" #message for good night
    bot.reply_to(message, greet)
  
  elif "namaste" in request or "namaskara" in request or "namaskar" in request:
    greet = "Namaskara, aap kaisesy hai?" #message for Namastey
    bot.reply_to(message, greet)


  elif "who" in request and "you?" in request:
    about = "Hi My name is Dragon. I am created using Python language by Fantastic Four(students of IIT Ropar) and My first version was created in May 2022." #message which tells about bot
    bot.reply_to(message, about)

  elif "who" in request and "you" in request:
    about = "Hi My name is Dragon. I am created using Python language by Fantastic Four(students of IIT Ropar) and My first version was created in May 2022." #message which tells about bot
    bot.reply_to(message, about)

  elif "yourself" in request:
    about = "Hi My name is Dragon. I am created using Python language by Fantastic Four(students of IIT Ropar) and My first version was created in May 2022."  #message which tells about bot
    bot.reply_to(message, about)

  elif "yourself?" in request:
    about = "Hi My name is Dragon. I am created using Python language by Fantastic Four(students of IIT Ropar) and My first version was created in May 2022."   #message which tells about bot
    bot.reply_to(message, about)
    
  elif "why"in request and "built" in request:
    cause="I am a project created by fantastic four (students of IIT Ropar) I hope I works well." #message which tells about why bot was built
    bot.reply_to(message, cause)

  elif "how" in request and "you?" in request:
    how = "Hey! I am great! thanks for asking."  #message for how are you
    bot.reply_to(message, how) 

  elif "how" in request and "you" in request:
    how = "Hey! I am great! thanks for asking." #message for how are you
    bot.reply_to(message, how)

  elif "where" in request and "you" in request:
    place = "So, turn left from the paanwaala and then go straight till you see a banyan tree. \njust kidding,I live in the cloud ;) "   #message for where are you
    bot.reply_to(message, place)

  elif "where" in request and "you?" in request:
    place = "So, turn left from the paanwaala and then go straight till you see a banyan tree. \njust kidding,I live in the cloud ;) "   #message for where are you
    bot.reply_to(message, place)

  elif "you" in request and "intelligent" in request :
    ans = "Well, when I was at school, I had to cheat on my metaphysics exam by looking into the soul of the boy next to me" #answer for you are intelligent
    bot.reply_to(message, ans)

  elif "you" in request and "intelligent?" in request :
    ans = "Well, when I was at school, I had to cheat on my metaphysics exam by looking into the soul of the boy next to me" #answer for you are intelligent
    bot.reply_to(message, ans)

  elif "how" in request and "old" :
    ans = "They say that age is nothing but a number. But technically, it’s also a word." #answer for age
    bot.reply_to(message, ans)

  elif "what" in request and "age" :
    ans = "They say that age is nothing but a number. But technically, it’s also a word." #answer for age
    bot.reply_to(message, ans)

  elif "what" in request and "age?" :
    ans = "They say that age is nothing but a number. But technically, it’s also a word." #answer for age
    bot.reply_to(message, ans)
    
  elif "favorite" in request and "colour" in request :
    ans = "My favorite color is … well, I don’t know how to say it in your language. It’s sort of greenish, but with more dimensions." #answer for favourite colour
    bot.reply_to(message, ans)

  elif "pick-up" in request and "line" in request :
    ans = "How about … Was your father an intergalactic space smuggler, wanted for peddling extraterrestrial contraband in nine systems? Then who stole the stars and put them in your eyes?" #answer for pick-up lines
    bot.reply_to(message, ans)

  elif "pick" in request and "line" in request :
    ans = "How about … Was your father an intergalactic space smuggler, wanted for peddling extraterrestrial contraband in nine systems? Then who stole the stars and put them in your eyes?" #answer for pick-up lines
    bot.reply_to(message, ans)

  elif "pick" in request and "lines" in request :
    ans = "How about … Was your father an intergalactic space smuggler, wanted for peddling extraterrestrial contraband in nine systems? Then who stole the stars and put them in your eyes?" #answer for pick-up lines
    bot.reply_to(message, ans)
  
  elif "doing" in request:
    doing = "I am dreaming about you :)" #answer for what are you doing
    bot.reply_to(message, doing)
    
  #URL code are attached here,so that the desired website can open just by entering it's name.    
  elif "youtube" in request:
    bot.reply_to(message, "https://www.youtube.com/") #URL for YouTube

  elif "instagram" in request:
    bot.reply_to(message, "https://www.instagram.com/") #URL for Instagram

  elif "linkedin" in request:
    bot.reply_to(message, "https://www.linkedin.com/")  #URL for LinkedIn

  elif "facebook" in request:
    bot.reply_to(message, "https://www.facebook.com/")    #URL for Facebook
  
  elif "twitter" in request:
    bot.reply_to(message, "https://www.twitter.com/") #URL for Twitter
  
  elif "whatsapp" in request:
    bot.reply_to(message, "https://www.whatsapp.com/") #URL for WhatsApp
  
  elif "gmail" in request or "email" in request:
    bot.reply_to(message, "https://mail.google.com/") #URL for Gmail

  elif "weather" in request:  #If weather in request then weather function will work
    try:
      ans = weather(message)
      bot.reply_to(message, ans)
    except:
      None

# Weather function starts here
@bot.message_handler(func = weather_message)
def weather(message):
  '''This will reply to the message which contains the weather keyword along with a city name and return the weather information to the user'''
  
  request = message.text.split() #Splitting the message
  
  for i in range(len(request)): #Making the message in lowercase
    request[i] = request[i].lower()

  city = request[1]
  
  try: # Try for the correct city name and if its true then return the required weather information
    complete_url ='https://api.openweathermap.org/data/2.5/weather?q=' + city +'&appid=d850f7f52bf19300a9eb4b0aa6b80f0d'
  
    response = requests.get(complete_url)
    x = response.json()
    y = x["main"]
    current_temperature = y["temp"]
    z = x["weather"]
    weather_description = z[0]["description"]
    bot.reply_to(message, "City: "+ city +"\n" + "Temperature: "+ str("{:.2f}".format(current_temperature - 273)) + u"\N{DEGREE SIGN}" +"C" + " (" + str(weather_description) + ")")

  except: #if the city name is not correct then return None
    return None
    

keep_alive()  #calling the keep_alive function for the bot to be run 24/7
bot.polling() #bot.polling for checking the messages constantly