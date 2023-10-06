from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
import json

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
    
def words(request):
    words = Word.objects.all()
    return render(request, 'words.html', {'words': words})

def concordances(request):
    exercise_list = []
    for concordance in Concordance.objects.all():
        exercise_list.append(concordance)
    return render(request, 'concordances.html', {'exercises': exercise_list})


def exercises_to_json(request):
    exercises = []
    for exercise in ConcordanceExercise.objects.all():
        exercises.append({
            'id': str(exercise.id),
            'question': exercise.question,
            'correct_answer': exercise.correct_answer,
            'wrong_answer': exercise.wrong_answer,
            'prompt': exercise.prompt,
            'type': 'cloze',
        })
    for concordance in Concordance.objects.all():
        exercises.append({
            'id': str(exercise.id),
            'front': concordance.english,
            'back': concordance.arabic,
            'type': 'flashcard',
            'prompt': 'Translate the following sentence:',
        })
        exercises.append({
            'id': str(exercise.id),
            'front': concordance.arabic,
            'back': concordance.english,
            'type': 'flashcard',
            'prompt': 'Translate the following sentence:',
        })
        
    for word in Word.objects.all():
        exercises.append({
            'id': str(exercise.id),
            'front': word.english,
            'back': word.arabic,
            'type': 'flashcard',
            'prompt': 'Translate the following word:',
        })
        exercises.append({
            'id': str(exercise.id),
            'front': word.arabic,
            'back': word.english,
            'type': 'flashcard',
            'prompt': 'Translate the following word:',
        })
        
    for sentence in SentenceVariation.objects.all():
        exercises.append({
            'id': str(exercise.id),
            'front': sentence.english,
            'back': sentence.arabic,
            'type': 'flashcard',
            'prompt': 'Translate the following sentence:',
        })
        exercises.append({
            'id': str(exercise.id),
            'front': sentence.arabic,
            'back': sentence.english,
            'type': 'flashcard',
            'prompt': 'Translate the following sentence:',
        })
        
    main_sentences = []
    
    for main_sentence in MainSentence.objects.all():
        
        sentence_children = []
        
        for sentence_variation in SentenceVariation.objects.filter(mainSentence=main_sentence):
            sentence_children.append(str(sentence_variation.id))
            
            for word in Word.objects.filter(sentenceVariations=sentence_variation):
                sentence_children.append(str(word.id))
                
                for concordance in Concordance.objects.filter(words=word):
                    sentence_children.append(str(concordance.id))
                    
                    for exercise in ConcordanceExercise.objects.filter(concordance=concordance):
                        sentence_children.append(str(exercise.id))
        print(sentence_children, '\n\n-----------------\n')       
        
        if len(sentence_children) > 3:
        
            main_sentences.append({
                'id': str(main_sentence.id),
                'english': main_sentence.english,
                'arabic': main_sentence.arabic,
                'children': sentence_children,
            })
        
    return HttpResponse(json.dumps({'exercises': exercises, 'main_sentences': main_sentences}), content_type="application/json")