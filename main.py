import numpy as np
import librosa

# Load the audio files
y1, sr1 = librosa.load('full.wav')
y2, sr2 = librosa.load('record.wav')

# It's important that the sample rates match - if they don't, you can resample.
if sr1 != sr2:
    y2 = librosa.resample(y2, sr2, sr1)
    
# Cross-correlate the signals
xcorr = np.correlate(y1, y2, mode='full')

# Find the lag that maximizes the cross-correlation
lag = np.argmax(xcorr)

# Convert lag to seconds
lag_in_seconds = lag / sr1

print(f"The most similar part to b.wav starts at {lag_in_seconds} seconds into a.wav.")
