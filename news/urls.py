from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import ListArticleView, DetailArticleView,CommentaireCreateView, CommentaireUpdateView, CommentaireDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inscription/', views.inscription, name ='inscription'),
    path('', views.accueil, name='accueil'),
    path('articles/', ListArticleView.as_view(), name='liste_articles'),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='detail'),
    path('article/<int:pk>/commentaire/ajouter/', CommentaireCreateView.as_view(), name='creation_com'),
    path('commentaire/<int:pk>/modifier/', CommentaireUpdateView.as_view(), name='modification_com'),
    path('commentaire/<int:pk>/supprimer/', CommentaireDeleteView.as_view(), name='suppression_com'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)