from django.contrib import admin
from .models import *


# all models are registered here
admin.site.register(Topic)
admin.site.register(MainSentence)
admin.site.register(SentenceVariation)
admin.site.register(Word)
admin.site.register(Concordance)
admin.site.register(ConcordanceExercise)