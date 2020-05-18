from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request,slug, template_name = 'idcomplete/index.html'):
    identite   =get_object_or_404(IdentiteComplete,slug=slug)
    persone   =  get_object_or_404(Person, slug=slug )
    identite.user = request.user
    persone.user = request.user
    return render(request, template_name, {'identite': identite,
                                            'persone':persone })


@login_required
def createIdc(request):
    if request.method == "POST":
        form = IdentiteCompleteForm(request.POST)
        if form.is_valid():
            id_compl= form.save(commit=False)
            id_compl.user = request.user
            id_compl.save()
            return redirect('home')
    else:
        form = IdentiteCompleteForm()
    return render(request, 'account/form.html', {'form': form})



