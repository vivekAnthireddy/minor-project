from SpeechRecognition import speech
from sel import search
from execute import fileopen



def assist():
    text = speech()
    print("You said : ", text)
    text = text.split(" ")
    if text[0] == 'search':
        temp = ' '.join(text[1:])
        search(temp)
    elif text[0] == 'open' and "." in text[-1]:
        temp = ' '.join(text[1:])
        search(temp)
    elif text[0] == 'open':
        temp = ' '.join(text[1:])
        fileopen(temp)
    else:
        print("Sorry Unable to recognize any command try including"+'\n'+"search than sentence you want to search "+'\n'+"open than filename"+'\n'+'')



if __name__ == '__main__':
    assist()