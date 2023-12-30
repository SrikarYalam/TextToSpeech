""" GENERATE SOUNDS
    Srikar Yalam
    Used to generate all possible sounds in their context word
    @requires epitran (eng-latn)
"""

import epitran

epi = epitran.Epitran('eng-Latn')
file = open('MIT_wordlist')
write_file = open('PossibleSounds_MIT', 'r+')
print('Using MIT Word List to generate possible sounds... ')

for word in file:
    write_file.write(epi.transliterate(f'{word}'))

file.close()
write_file.close()
print('done')
    
