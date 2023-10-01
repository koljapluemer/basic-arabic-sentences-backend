import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentences.settings")
import django
django.setup()
from sentenceBank.models import *

from tashaphyne.stemming import ArabicLightStemmer
ArListem = ArabicLightStemmer()

Word.objects.all().delete()

word_list = []
# go through MainSentences, SentenceVariations, Concordances
# for each object, split the Arabic into words and print words
for mainSentence in MainSentence.objects.all():
    if mainSentence.arabic:
        words = mainSentence.arabic.split(' ')
        # filter only words that are not ' ' or '...'
        words = [word for word in words if word not in [' ', '...', ''] and len(word) > 2]
        
        for word in words:
            # remove punctuation
            word = word.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(';', '').replace(':', '').replace('؟', '').replace('،', '')
            stem = ArListem.light_stem(word)
            
            stemmed_word = ArListem.get_stem() 
            # find or create Word with arabic=stemmed_word
            word_obj, created = Word.objects.get_or_create(arabic=stemmed_word)
            word_obj.mainSentences.add(mainSentence)