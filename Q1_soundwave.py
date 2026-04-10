##consider a sound signal transform the signal in such a way that when played it sounds in (a) 2x speed (b)1/2x speed

import soundfile as sf
import scipy.signal as signal

# Read input audio
audio, fs = sf.read("input.wav")

# (a) 2x speed
audio_2x = signal.resample(audio, len(audio) // 2)
sf.write("output_2x.wav", audio_2x, fs)

# (b) 0.5x speed
audio_half = signal.resample(audio, len(audio) * 2)
sf.write("output_half.wav", audio_half, fs)
