import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentences.settings")
import django
django.setup()
from sentenceBank.models import *


# open autotranslation1.txt
# read each line and split at ;
# match a Django object with english propert corresponding to the first item in the split
# set the arabic property of that object to the second item in the split:

with open(os.path.join(os.path.dirname(__file__), 'autotranslation1.txt'), 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            split_line = line.split(';')
            english = split_line[0]
            arabic = split_line[1]
            print(english)
            print(arabic)
            print()
            try:
                mainSentence = MainSentence.objects.get(english=english)
                mainSentence.arabic = arabic
                mainSentence.save()
            except:
                try:
                    sentenceVariation = SentenceVariation.objects.get(english=english)
                    sentenceVariation.arabic = arabic
                    sentenceVariation.save()
                except:
                    try:
                        word = Word.objects.get(english=english)
                        word.arabic = arabic
                        word.save()
                    except:
                        try:
                            concordance = Concordance.objects.get(english=english)
                            concordance.arabic = arabic
                            concordance.save()
                        except:
                            print(f"couldn't find {english} in any of the models")
                            print()
                            continue