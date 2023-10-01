import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentences.settings")
import django
django.setup()
from sentenceBank.models import *

# open word-translation1.txt
# for each line, split at ;
# match the Word object with Arabic property corresponding to the first item in the split
# set the english property of that object to the second item in the split:

with open(os.path.join(os.path.dirname(__file__), 'word-translation1.txt'), 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            split_line = line.split(';')
            arabic = split_line[0]
            english = split_line[1]
            print(arabic)
            print(english)
            print()
            try:
                word = Word.objects.get(arabic=arabic)
                word.english = english
                word.save()
            except:
                print(f"couldn't find {arabic} in any of the Word objects")
                print()
                continue