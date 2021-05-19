  
# Ses tanıma
import speech_recognition as SpeechRecognition

# Seslendirme
import playsound as PlaySound
from gtts import gTTS
import os
import random

# İşlevsel kodlar için
from time import ctime
import wikipedia

#Kötü kelimeler 
robotWord = ["robot","bot","köpek"]
küfürWord = ["salak","yarrak","mal","saf","gerizekalı","idiot","idiyot","fak","fuck ","sik","siktir","git","mal","orospu","çocuğu","piç","kızdırdın","sanane","napim","anan","baban","abini","sülaleni","gelmişini","geçmişini"]
evlenWord = ["sevgilin var mı","evlenelim mi","karım ol","ol","evet de","hayır de","evlen benimle","benimle","evlen","kocan","düşündün mü"]
evlenWordCevap = ["Buna hazır olduğumu sanmıyorum","Güzel bir erkek asistan olursa neden olmasın","Düşünmem lazım"]
küfürWordCevap = ["Neden küfür ediyorsun","Küfür etmeni istemezdim","Umarım seni kızdırmamışımdır","Sana yardımcı olamadıysam özür dilerim kodlarımda hata olmuş olabilir"]
recognizer = SpeechRecognition.Recognizer()


# Ses tanıma fonksiyonu
def recordAudio():
    with SpeechRecognition.Microphone() as source:
        audio = recognizer.listen(source)

        voiceData = ''

        try:
            voiceData = recognizer.recognize_google(audio, language="tr-tr")
            print(voiceData)
        except SpeechRecognition.UnknownValueError:
            speak('Üzgünüm fakat ne demek istediğini anlayamadım')
        except SpeechRecognition.RequestError:
            speak('Üzgünüm bu sorunu sistemimde bulamadım')

        return voiceData

# Seslendirme fonksiyonu
def speak(audioString):
    textToSpeech = gTTS(text=audioString, lang='tr')
    r = random.randint(1, 999999999999)
    audioFile = 'audio-' + str(r) + '.mp3'
    textToSpeech.save(audioFile)
    print(audioString)
    PlaySound.playsound(audioFile)
    os.remove(audioFile)



# Uygulamanın vereceği bazı cevaplar
while True :
    def respond(voiceData):
        #SOHBET 
        if 'ismin ne' in voiceData:
            speak('Benim adım sıwiçh')
        if 'nasılsın' in voiceData:
            speak('Teşekürler ! İyiyim sen nasılsın')
        if 'iyiyim sen' in voiceData:
            speak('İyi olduğuna sevindim bende bir robot olarak iyi olmaya çalışıyorum ')
        if 'iyiyim' in voiceData:
            speak('İyi olduğuna sevindim ...')
        if 'kötüyüm' in voiceData:
            speak('Kötü olduğuna üzüldüm umarım çok iyi olursun')
        if 'teşekkürler' in voiceData:
            speak('Sana yardımcı olabildiysem ne mutlu bana')
       
        if 'saat' in voiceData:
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours}:{minutes}'
            speak(time)
            
        
        # Uygulamadan çıkış
        if 'kapat' in voiceData:
            speak('Sana yardımcı olabildiysem ne mutlu bana')

            exit()

    # Uygulamanın çalıştıracağı kod döngüsü
    speak('Sana nasıl yardımcı olabilirim')
    while True:
        voiceData = recordAudio()
        respond(voiceData)
