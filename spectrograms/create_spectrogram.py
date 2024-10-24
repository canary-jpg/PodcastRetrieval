import librosa
import numpy as np
from matplotlib import pyplot as plt
from librosa import display
# getting spectrogram data from librosa from podcast audio data
audio_file = './speech.mp3'
y, sr = librosa.load(audio_file)
duration = float(len(y))/sr
print(duration)
# using librosa.stft to convert audio sample to frequency domain
fourier = np.abs(librosa.stft(y, n_fft=512, center=False, hop_length=1024))*2
print(fourier)

plt.figure(figsize=(12, 8))
display.specshow(librosa.amplitude_to_db(fourier, ref=np.max),
                 y_axis='log', x_axis='time')
plt.title("Sample Spectrogram")
plt.colorbar(format='%+0.2f dB')
plt.tight_layout()
plt.show()
