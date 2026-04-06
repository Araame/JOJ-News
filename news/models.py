from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=50)
    def __str__(self):
        return self.nom
    

class Commentaire(models.Model):
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    derniere_maj = models.DateTimeField(auto_now=True)
    commentateur = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name="commentaires", null=True, blank=True)  


    def __str__(self):
        return self.contenu

class Article(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now=True)
    derniere_maj = models.DateTimeField(auto_now=True)
    banniere = models.ImageField(upload_to='images/')
    categories = models.ManyToManyField(Categorie)
    createur = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre


    