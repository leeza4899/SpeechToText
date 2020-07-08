
import speech_recognition as SRG 
import time
 
store = SRG.Recognizer()
with SRG.Microphone() as s:
     
    print("Recording for the next 7 seconds.\n")
    print("Recording time:",time.strftime("%m/%d/%Y ---> %I:%M:%S %p"))
     
    audio_input = store.record(s, duration=7)
    print("Finished Recording\n");
    
    try:
        text_output = store.recognize_google(audio_input)
        print(text_output + "\n")
        print("Finished printing")
 
        print("Execution time:",time.strftime("%m/%d/%Y ---> %I:%M:%S %p"))
    except:
           print("Couldn't process the audio input.")

