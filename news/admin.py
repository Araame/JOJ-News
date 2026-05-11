from django.contrib import admin
from .models import Article, Categorie, Commentaire


class ArticleAdmin(admin.ModelAdmin):
    
    #Affiche les champs d'un article dans l'interface
    list_display = ('createur', 'titre', 'contenu', 'date_creation')

    #Filtrer les champs d'un article dans l'interface
    list_filter = ('createur', 'date_creation')

    #Ordonne les articles dans l'interface
    ordering = ('-date_creation',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Commentaire)
admin.site.register(Categorie)