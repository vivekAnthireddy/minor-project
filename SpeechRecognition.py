import speech_recognition as sr
import time

def speech():
    r = sr.Recognizer()
    #print(r.dynamic_energy_threshold,'\n',r.energy_threshold)
    r.dynamic_energy_threshold=False
    r.energy_threshold=400
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        print("recognising done")
    try:
        print("converting audio to text ...")
        temp= r.recognize_google(audio)

    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return "Could not request results; {0}".format(e)
    return temp





if __name__ == '__main__':
    text=speech()
    print(text)




