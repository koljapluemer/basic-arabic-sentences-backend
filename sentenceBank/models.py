from django.db import models
import uuid

# Create your models here.
class Topic(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
DIALECTS = (
    ('MSA', 'MSA'),
    ('Egyptian', 'Egyptian'),
)    
    
class MainSentence(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    english = models.CharField(max_length=500)
    arabic = models.CharField(max_length=500, blank=True, null=True)
    dialect = models.CharField(max_length=50, choices=DIALECTS, default='MSA')

    def __str__(self):
        return f"{self.english} - {self.arabic}" if self.english and self.arabic else self.english or self.arabic or ""

    
class SentenceVariation(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    mainSentence = models.ForeignKey(MainSentence, on_delete=models.CASCADE)
    english = models.CharField(max_length=500)
    arabic = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.english} - {self.arabic}" if self.english and self.arabic else self.english or self.arabic or ""

    
class Word(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    sentenceVariations = models.ManyToManyField(SentenceVariation)
    mainSentences = models.ManyToManyField(MainSentence)
    english = models.CharField(max_length=500)
    arabic = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.english} - {self.arabic}" if self.english and self.arabic else self.english or self.arabic or ""

    
class Concordance(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    words = models.ManyToManyField(Word)
    english = models.CharField(max_length=500)
    arabic = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return f"{self.english} - {self.arabic}" if self.english and self.arabic else self.english or self.arabic or ""

    
class ConcordanceExercise(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    concordance = models.ForeignKey(Concordance, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    prompt = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=500)
    wrong_answer = models.CharField(max_length=500, blank=True, null=True)
    def __str__(self):
        return self.question