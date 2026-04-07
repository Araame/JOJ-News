from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView
from .models import Article, Commentaire
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.
def accueil(request):
    return render(request, "accueil.html", context = {})

def inscription(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/inscription.html', {'form': form})



class ListArticleView(ListView):
    model = Article
    template_name = 'blog.html'  
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.prefetch_related('commentaires').all()




class DetailArticleView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article'




class CommentaireCreateView(LoginRequiredMixin, CreateView):
    model = Commentaire
    fields = ['contenu'] 
    template_name = 'form.html'

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        
        form.instance.article = article
        form.instance.commentateur = self.request.user
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})
    


class CommentaireUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Commentaire
    fields = ['contenu'] 
    template_name = 'form.html'

    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.commentateur

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.article.pk})



class CommentaireDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Commentaire
    template_name = 'suppression.html'


    def test_func(self):
        commentaire = self.get_object()
        return self.request.user == commentaire.commentateur

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.article.pk})