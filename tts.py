""" TTS class
    Srikar Yalam
    @requires epitran, pydub
    Allows tts prompt
"""

import epitran
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import speedup, normalize


def get_tts_sound(epi, prompt):
    sentence = (epi.transliterate(f'{prompt}'))
    print(f'sentence: {sentence}')


    spoken = AudioSegment.from_file("wav_files/space.wav", format='wav')

    for letter in sentence:
        try: 
            if letter == ' ':
                spoken += AudioSegment.from_file("wav_files/space.wav", format='wav')
            else:
                spoken += AudioSegment.from_file(f'wav_files/{letter}.wav', format='wav')
        except:
            spoken += AudioSegment.from_file("wav_files/space.wav", format='wav')
            

    speed = speedup(spoken, 2, 150)
    normalized = normalize(speed)
    return normalized
