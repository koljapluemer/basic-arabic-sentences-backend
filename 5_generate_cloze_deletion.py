import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sentences.settings")
import django
import random
django.setup()
from sentenceBank.models import *

# ConcordanceExercise.objects.all().delete()

deleted_words = []

for concordance in Concordance.objects.all():
    # generate three cloze deletion exercises
    for i in range(3):
        # replace a random word from arabic with ؟؟؟
        deleted_word = concordance.arabic.split()[random.randint(0, len(concordance.arabic.split())-1)]
        cloze_deletion = concordance.arabic.replace(deleted_word, "؟؟؟")
        
        exercise, created = ConcordanceExercise.objects.get_or_create(
                concordance=concordance, 
                prompt='Choose the word that best completes the sentence:',
                correct_answer=deleted_word,
                question=cloze_deletion
        )
        deleted_words.append(deleted_word)
        

# loop again, randomly pick from deleted_words as wrong answers
for exercise in ConcordanceExercise.objects.filter(wrong_answer__isnull=True):
    exercise.wrong_answer = random.choice(deleted_words)
    exercise.save()