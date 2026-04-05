from django.contrib import admin
from .models import Article, Categorie, Commentaire


# Register your models here.
admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(Categorie)