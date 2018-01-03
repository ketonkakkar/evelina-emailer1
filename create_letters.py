import commands
import datetime
import os
import smtplib
import sys

def split_into_letters():
    filepath = 'evelina.txt'
    letter_positions = []
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if "LETTER" in line:
                letter_positions.append(cnt)

    letter_positions.append(cnt)
    with open(filepath) as fp:
        evelina = fp.readlines()
    if not os.path.exists("letters"):
        os.mkdir("letters")
    for i in range(0, len(letter_positions) - 1):
        start = letter_positions[i]
        end = letter_positions[i+1]
        letter_name = "LETTER_%d" % (i+1)
        letter_path = "letters/" + letter_name + ".txt"
        with open(letter_path, 'w') as l:
            l.write(''.join(evelina[start:end]))
            
split_into_letters()