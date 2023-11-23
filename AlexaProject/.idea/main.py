#Part 1 :Take User Voice And Convert Into Text
#Part 2 :Process The Text And Give Some Result(in the form of text)
#Part 3 :Convert The Result(text) Into Voice

#Part 1(speech regonition lib install )
import speech_recognition as sr
import pyttsx3 #used to convert text to speech
import pywhatkit #it is used to performSend WhatsApp messages.Play a YouTube video.
import wikipedia #Perform a Google Search.Get information on a particular topic.
import datetime as dt
import pyjokes  #give jokes related to programmig


def talkaction(answer):  #function to convert text to speach and give o/p to user
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # voices[0].id = male,voices[1].id= female
    engine.say(answer) #answer varies for differnt different questions so we dint give "i am waiting for ur que etcc.
    engine.runAndWait()


def processQuestion(question):
        if 'what are you doing' in question:
            print('I Am Waiting For Your question')
            talkaction("I Am Waiting For Your question") #fnction call name of function is talkaction tht function converts text to voice and give o/p
            return True

        elif 'how are you' in question:
            print('i am good thank you.How can i help you?')
            talkaction('i am good thank you.How can i help you?')
            return True

        elif 'play'in question:
            question = question.replace('play','')
            pywhatkit.playonyt(question)
            return True

        elif 'who is' in question:
            question = question.replace('who is','')
            print(wikipedia.summary(question,1))# 1 represents how many sentence it can be 2 3 4 etc
            talkaction(wikipedia.summary(question,1))
            return True
        elif 'date' in question:
            date = dt.date.today()
            print(date)
            talkaction(date)
            return True
        elif 'joke' in question:
            joke =  pyjokes.get_joke()
            print(joke)
            talkaction(joke)
            return True

        elif 'love you' in question:
            talk("love to tooo")
            return True

        elif 'college' in question:
            question = question.replace('college', '')
            print(wikipedia.summary(question, 1))  # 1 represents how many sentence it can be 2 3 4 etc
            talkaction(wikipedia.summary(question, 1))
            return True

        elif 'bye' in question:
            talkaction("bye bye,please take care we will meet later")
            return False

        else:
            print("i didn't get your question can you say it again")
            return True

def getQuestion():
    r=sr.Recognizer() #listens what user talks in microphone


    with sr.Microphone() as source:
        print('say something')
        audio=r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            print(r.recognize_google(audio))
            question = r.recognize_google(audio)
            if 'Alexa' in question:
                question = question.replace('Alexa', '')
                print(question)
                return question
            else:
                print("you are not talking with me u contiue your work")
                return "notwithme"

        except sr.UnknownValueError:
            print("sorry i can't get your question")

canAskQuestion = True # true means to ask any number of question
while canAskQuestion:
    question = getQuestion()
    if(question == "notwithme"):
        talkaction("ok carry on with your friends,bye!")
        canAskQuestion=False
    else:
        canAskQuestion = processQuestion(question)



