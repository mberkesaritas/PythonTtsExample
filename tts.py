import numpy as np
import speech_recognition as sr
import pyttsx3
import sounddevice 
from scipy.io.wavfile import write 
from os import system
import webbrowser

frame = []
fps = 44100
duration = 3
r = sr.Recognizer()
fileName = "output.wav"
system("say Merhaba Ben Berke Tarafından geliştirilmiş bir yapay zekayım.Sen kimsin ?")

def recording(): 
    print('\033[92m' + "Sizi dinliyorum...")
    recording = sounddevice.rec(int(duration*fps),samplerate = fps , channels = 1,dtype = np.int32)
    sounddevice.wait()
    print('\033[92m' + "Anlaşıldı...")
    write("output.wav",fps,recording)


def stt() : 
    with sr.AudioFile(fileName) as source:
        # listen for the data (load audio to memory)
        audioData = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audioData,language = "tr-TR")
        print('\033[92m' + text)
        if(text == "berke" or text == "Berke"):
            print('\033[92m' + "❤️  Berke  ❤️")
            system("say Hoşgeldin patron .Sen olduğunu fark edemedim !! Sana nasıl yardımcı olabilirim iki gözümün çiçeği ?")
            recording()
            with sr.AudioFile(fileName) as source:
                # listen for the data (load audio to memory)
                audioData = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_google(audioData,language = "tr-TR")
                print(text)
                if(text == "tarayıcıyı aç" or text == "Tarayıcıyı aç") : 
                    system("say Hemen hallediyorum dünyanın en yakışıklı insanı")
                    webbrowser.get("safari").open("www.google.com")
                    system("say Başka bir şey yapmamı ister misin gönlümün sahibi ?")
                    recording()
                    with sr.AudioFile(fileName) as source:
                        # listen for the data (load audio to memory)æ
                        audioData = r.record(source)
                        # recognize (convert from speech to text)
                        text = r.recognize_google(audioData,language = "tr-TR")
                        print(text)
                        if(text == "evet" or text == "Evet"):
                            system("say Sen yeterki iste, her şeyi yaparım")

                elif (text == "Bana şiir oku" or text == "bana şiir oku"or text == "bana Şiir oku"):
                    system("say Tabii okuyorum ,    Kaşların yay ,  kirpiklerin ok , vurduğunu öldürürsün, geçme mescit yanlarından , çok namaz böldürürsün... ha,ha,ha")
                elif (text == "bana özlü söz söyle" or text == "Bana özlü söz söyle"):
                    system("say Sen yeterki iste, her şeyi yaparım")
                    system("say gök yüzünde bir yıldız olsam ilk sana kayardım")


                else : 
                    system("say Anladığımı sanmıyorum")
                
        else : 
            system("say Üzgünüm !! Sizi tanımıyorum")
        


recording()    
stt()
