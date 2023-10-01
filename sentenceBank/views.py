from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *



def index(request):
    exercise_list = []
    # add all MainSentences, all SentenceVariations, all Concordances and all Words to exercise_list:
    for mainSentence in MainSentence.objects.all():
        exercise_list.append(mainSentence)
    for sentenceVariation in SentenceVariation.objects.all():
        exercise_list.append(sentenceVariation)
    for concordance in Concordance.objects.all():
        exercise_list.append(concordance)
    for word in Word.objects.all():
        exercise_list.append(word)
        
    return render(request, 'list.html', {'exercise_list': exercise_list})
    