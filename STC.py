import io
import argparse
from google.oauth2 import service_account
import speech_recognition as sr
from fuzzywuzzy import fuzz
Str1=str(input("Enter the statement:"))
#credentials=service_account.Credentials.from_service_account_file('speech-273706-b59bc46a664b.json ',scopes=["https://www.googleapis.com/auth/cloud-platform"])

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`
    Str2=r.recognize_google(audio)
    print("You said: " + r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

def ratio_confidence(a,b):
    Ratio = fuzz.ratio(a.lower(),b.lower())
    Partial_Ratio = fuzz.partial_ratio(a.lower(),b.lower())
    Token_Sort_Ratio = fuzz.token_sort_ratio(a.lower(),b.lower())
    Token_Set_Ratio = fuzz.token_set_ratio(a.lower(),b.lower())
    ratios=[Ratio,Partial_Ratio,Token_Sort_Ratio,Token_Set_Ratio]
    max_ratio=max(ratios)
    return max_ratio , Token_Set_Ratio

confidence,voice=ratio_confidence(Str1,Str2)

print("Confidence Interval :",confidence)
print("Voice Recognition Accuracy :",voice)
    
