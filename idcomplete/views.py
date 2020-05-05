from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


def home_view(request, pk, template_name = 'idcomplete/index.html'):
	id    =   get_object_or_404(IdentiteComplete, pk = pk)
	return render(request, template_name, {'id': id })


@login_required
def createIdc(request):
    if request.method == "POST":
        form = IdentiteCompleteForm(request.POST)
        if form.is_valid():
            identite = form.save(commit=False)
            identite.author = request.user
            identite.save()
            return redirect('http://127.0.0.1:8000')
    else:
        form = IdentiteCompleteForm()
    return render(request, 'account/form.html', {'form': form})

