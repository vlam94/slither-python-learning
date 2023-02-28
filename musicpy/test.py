from pydub import AudioSegment
from pydub.generators import Sine, Square
import random

# Define the tempo of the track in beats per minute
tempo = 140

# Define the length of each beat in milliseconds
beat_length = int(30000 / tempo)

# Generate a 30 second track
duration = 30 * 1000

# Create a silence of half a beat at the start of the track
intro = AudioSegment.silent(duration=beat_length//2)

# Generate the main melody using sine waves
melody = AudioSegment.from_mono_audiosegments(*[Sine(440 * int(2 ** (n / 12)), 44100)
                                                   .to_audio_segment(duration=int(beat_length // 4))
                                                   .apply_gain(-6)
                                                  for n in [0, 2, 4, 7]] * (duration // beat_length // 4))
# Generate a second melody using square waves
melody2 = AudioSegment.from_mono_audiosegments(*[Square(330 * int(2 ** (n / 12)), 22050)
                                                    .to_audio_segment(duration=beat_length // 4)
                                                    .apply_gain(-6)
                                                   for n in [0, 4, 7, 11]] * (duration // beat_length // 4))

# Randomly pan the melodies left and right
melody = melody.pan(random.uniform(-1, 1))
melody2 = melody2.pan(random.uniform(-1, 1))

# Mix the two melodies together
melody = melody.overlay(melody2)

# Generate a bassline using sine waves
bass = AudioSegment.from_mono_audiosegments(*[Sine(110 * int(2 ** (n / 12)))
                                                 .to_audio_segment(duration=beat_length // 2)
                                                 .apply_gain(-6)
                                                for n in [0, 2, 5]] * (duration // beat_length // 2))

# Generate the drums using square waves
drums = AudioSegment.from_mono_audiosegments(*[Square(660)
                                                  .to_audio_segment(duration=beat_length // 4)
                                                  .apply_gain(-6)
                                                 for i in range((duration // beat_length) // 4)])

# Mix the intro, melody, bass, and drums together
track = intro + melody.overlay(bass).overlay(drums)
track.export("test.wav", format="wav")
