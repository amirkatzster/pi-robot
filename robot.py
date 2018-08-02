from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play


mp3_fp = BytesIO()
tts = gTTS('I love you Anat. Maybe study instead of dealing with that mess')
tts.write_to_fp(mp3_fp)
tts.save('hello.mp3')

# mixer.init()
# mixer.music.load('hello.mp3')
# mixer.music.play()
# mixer.init()
# mixer.Sound(mp3_fp)

# AudioSegment.converter = 'C:\\dev\\GitHub\\pi-robot\\ffmpeg\\ffmpeg.exe'
# AudioSegment.ffmpeg = 'C:\\dev\\GitHub\\pi-robot\\ffmpeg\\ffmpeg.exe'
# song = AudioSegment.from_mp3(StringIO(mp3_fp))
# play(song)

# from gtts import gTTS
# tts = gTTS('Im not your fucking servent.. Go take your own water', lang='en')
# tts.save('hello.mp3')