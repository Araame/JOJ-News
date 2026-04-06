from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView
from .models import Article



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
    paginate_by = 5

    def get_queryset(self):
        return Article.objects.prefetch_related('commentaires').all()

class DetailArticleView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article'