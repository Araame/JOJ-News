from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import ListArticleView, DetailArticleView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inscription/', views.inscription, name ='inscription'),
    path('accueil/', views.accueil, name='accueil'),
    path('articles/', ListArticleView.as_view(), name='liste_articles'),
    path('article/<int:pk>/', DetailArticleView.as_view(), name='detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)