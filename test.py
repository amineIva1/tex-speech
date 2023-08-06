from elevenlabs import generate, play ,voices , stream
from elevenlabs import set_api_key
set_api_key("1ee0a06d7afb7079c9f7487f53449036")

voices = voices()
audio = generate(
  text="Hi! My name is Bella, nice to meet you!",
  voice=voices[1],
  model="eleven_monolingual_v1"
)

print(voices)
play(audio)