from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm


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