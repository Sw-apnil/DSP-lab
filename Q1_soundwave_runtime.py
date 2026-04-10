import os
import soundfile as sf
import sounddevice as sd
import numpy as np

# Get correct path to input.wav
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "input.wav")

# Read audio file
audio, fs = sf.read(input_path)

print("Playing original sound...")
sd.play(audio, fs)
sd.wait()

# (a) 2x speed 

audio_2x = audio[::2]   # take every 2nd sample

print("Playing 2x speed sound...")
sd.play(audio_2x, fs)
sd.wait()

# (b) 0.5x speed 
audio_half = np.repeat(audio, 2, axis=0)  # repeat each sample twice

print("Playing 0.5x speed sound...")
sd.play(audio_half, fs)
sd.wait()
