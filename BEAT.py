import numpy as np
import soundfile as sf # type: ignore

# Parameters for the audio file
sample_rate = 44100  # Samples per second
duration = 2         # Duration in seconds

# Generate time axis
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate a simple beat pattern
def generate_beat(frequency, length, sample_rate):
    return 0.5 * np.sin(2 * np.pi * frequency * np.linspace(0, length, int(sample_rate * length), endpoint=False))

# Create individual drum sounds
kick = generate_beat(60, 0.1, sample_rate)    # Kick drum sound
snare = generate_beat(180, 0.1, sample_rate)  # Snare drum sound
hi_hat = generate_beat(300, 0.05, sample_rate) # Hi-hat sound
silence = np.zeros(int(sample_rate * 0.05))   # Short silence

# Assemble the beat pattern
beat_pattern = np.concatenate([
    kick, silence, hi_hat, silence, # Bar 1
    silence, snare, hi_hat, silence,
    kick, silence, hi_hat, silence,
    silence, snare, hi_hat, hi_hat,

    kick, silence, hi_hat, silence, # Bar 2
    silence, snare, hi_hat, silence,
    kick, silence, hi_hat, silence,
    hi_hat, snare, hi_hat, silence,

    kick, silence, hi_hat, silence, # Bar 3
    silence, snare, hi_hat, silence,
    kick, silence, hi_hat, silence,
    silence, snare, hi_hat, hi_hat,

    kick, silence, hi_hat, silence, # Bar 4
    silence, snare, hi_hat, silence,
    kick, silence, hi_hat, silence,
    hi_hat, snare, hi_hat, silence
])

# Save the beat pattern as an MP3 file
sf.write('random_beat.wav', beat_pattern, sample_rate)

