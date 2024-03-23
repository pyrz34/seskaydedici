import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

#sampling frequency
freg = 44100

#Recording duration
duration = 5

#Start recorder with the given values
#of duration and sample frequency

recording = sd.rec(int(duration*freg),samplerate=freg,channels=2)

# Record audio for the given number of seconds
sd.wait()

write("recording0.wav",freg,recording)

wv.write("recording1.wav",recording,freg,sampwidth=2)