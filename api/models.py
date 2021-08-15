from django.db import models

# Create your models here.

class Book(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=50)
    annee_publication = models.CharField(max_length=10)
    pages = models.PositiveIntegerField()
    
    def __str__(self):
        return self.titre 
