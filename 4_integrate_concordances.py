import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentences.settings")
import django
django.setup()
from sentenceBank.models import *


# loop concordances1.txt
with open(os.path.join(os.path.dirname(__file__), 'concordances1.txt'), 'r') as f:
    word_obj = None
    for line in f:
        # if empty line, skip
        if not line.strip():
            continue
        # check if line does not start with a number
        if not line[0].isdigit():
            # if so, split at ;
            split_line = line.split(';')
            # get the arabic and english
            arabic = split_line[0].strip()
            # find or create Word object with arabic=arabic
            try:
                word_obj = Word.objects.get(arabic=arabic)
            except:
                print(f"couldn't find {arabic} in any of the Word objects")
                # MANUALLY delete whatever shows up here (including following concordances)
                
        else:
            # ignore the first three characters
            split_line = line[2:].split(';')
            # get the arabic and english
            arabic = split_line[0].strip()
            english = split_line[1].strip()
            # get or create Concordance object with english=english and arabic=arabic
            concordance_obj, created = Concordance.objects.get_or_create(english=english, arabic=arabic)
            # add word_obj to concordance_obj
            concordance_obj.words.add(word_obj)