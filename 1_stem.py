import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentences.settings")
import django
django.setup()
from sentenceBank.models import *

from tashaphyne.stemming import ArabicLightStemmer
ArListem = ArabicLightStemmer()

# Word.objects.all().delete()

word_list = []
# go through MainSentences, SentenceVariations
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
            
            # do the same for the unstemmed word
            word_obj, created = Word.objects.get_or_create(arabic=word)
            word_obj.mainSentences.add(mainSentence)
            
# same process for SentenceVariations
for sentenceVariation in SentenceVariation.objects.all():
    if sentenceVariation.arabic:
        words = sentenceVariation.arabic.split(' ')
        # filter only words that are not ' ' or '...'
        words = [word for word in words if word not in [' ', '...', ''] and len(word) > 2]
        
        for word in words:
            # remove punctuation
            word = word.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(';', '').replace(':', '').replace('؟', '').replace('،', '').replace(')', '').replace('(', '')
            stem = ArListem.light_stem(word)
            
            stemmed_word = ArListem.get_stem() 
            # find or create Word with arabic=stemmed_word
            word_obj, created = Word.objects.get_or_create(arabic=stemmed_word)
            word_obj.sentenceVariations.add(sentenceVariation)
            
            # do the same for the unstemmed word
            word_obj, created = Word.objects.get_or_create(arabic=word)
            word_obj.sentenceVariations.add(sentenceVariation)