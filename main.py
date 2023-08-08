import gradio as gr
import openai
from elevenlabs import generate, play
import soundfile as sf
from elevenlabs import set_api_key
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

set_api_key("1ee0a06d7afb7079c9f7487f53449036")
openai.api_key="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"
messages = [{"role": "system", "content": "You are a helpful assistant."}]

def transcribe(audio):
    # in python if we write only message python will create a local variable for the function transcribe when we add "global" it know that we are accessing/modifying the variable "messages"
    global messages
    
    audio_file= open(audio, "rb")
    # the transcrition of the audio by whisper 
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    # appending the transcript to the messages list
    messages.append({"role": "user", "content": transcript["text"]})
    # getting the response to the transcript from chatgpt
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    #defining the message that will be sento to chatgpt as my list of messages
    messages=messages
    )
    #chatgpt send a lot of info in its reponse . Here we select only the needed content from the message frome the 1st element of the response list 
    system_messages=response["choices"][0]["message"]["content"]
    #we append the response to the lsit of messages
    messages.append({"role": "assistant", "content":system_messages})
    #better format the messages for more readablility
    chat_transcript=""
    for msg in messages:
        if msg["role"]!="system":
            chat_transcript+=msg['role']+" :" +msg['content']+"\n\n"

    print(response)


    audio11 = generate(
    text=system_messages,
    voice="Bella",
    model="eleven_monolingual_v1"
    )
    
    play(audio11)
    # sf.write(audio11,"r.wav",samplerate=44100)
    # audio_output_filepath = "r.wav"

    #sentiment analysis
    Sentence=[str(transcript)]
    analyser=SentimentIntensityAnalyzer()
    sentiment=analyser.polarity_scores(Sentence)
      
    # return audio_output_filepath
    return sentiment

demo = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone",type="filepath"), outputs="text")
    
demo.launch() 
