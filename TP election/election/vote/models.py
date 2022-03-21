from django.db import models
from django.utils import timezone
import datetime

class Elections(models.Model):
    elections_name = models.CharField(max_length=50)
    publish_date = models.DateTimeField("date de la publication")
    
    def __str__(self):
        return self.elections_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    elections = models.ForeignKey(Elections,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Personnes(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    login = models.CharField(max_length=50)
    mdp = models.CharField(max_length=50)
    tel = models.CharField(max_length=20)
    date_naissance = models.DateTimeField("date de naissance")

class Coordonnees(models.Model):
    adresse = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    personnes = models.ForeignKey(Personnes,on_delete=models.CASCADE)

class Voter(models.Model):
    personnes = models.ForeignKey(Personnes,on_delete=models.CASCADE)
    elections = models.ForeignKey(Elections,on_delete=models.CASCADE)

