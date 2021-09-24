
from django.shortcuts import redirect, get_object_or_404, render
from deplacement.models import Tab_bords
from deplacement.forms import ArticleForm


def liste(request):
    
    minis = Tab_bords.objects.all()
   

    return render(request, 'liste.html', {"minis":minis})

def internal(request):

    return render(request,'internal.html')


def nouveau(request):
    
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            
            
    
    form = ArticleForm()

    return render(request,'deplacement.html',{'form': form})

def redirection(request, code):
    """ Redirection vers l'URL enregistrée """
    mini = get_object_or_404(MiniURL, code=code)
    mini.nb_acces += 1
    mini.save()

    return redirect(mini.url, permanent=True)


