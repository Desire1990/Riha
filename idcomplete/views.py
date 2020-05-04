from django.shortcuts import  render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
# from .tokens import account_activation_token
from django.template.loader import render_to_string
from .models import *
from .forms import *

def home_view(request, pk, template_name = 'idcomplete/index.html'):
	id    =   get_object_or_404(IdentiteComplete, pk = pk)
	return render(request, template_name, {'id': id })


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
    return render(request, 'idcomplete/form.html', {'form': form})





















































































































































































































































# from django.shortcuts import render
# from django.contrib.auth import authenticate, login, logout
# from django.http import *
# from .models import *
# from django.views.generic import TemplateView
# from django.conf import settings
# from .forms import RegisterForm

# class LoginView(TemplateView):

#   template_name = 'idcomplete/index.html'

#   def post(self, request, **kwargs):

#     username = request.POST.get('username', False)
#     password = request.POST.get('password', False)
#     user = authenticate(username=username, password=password)
#     if user is not None and user.is_active:
#         login(request, user)
#         return HttpResponseRedirect( settings.LOGIN_REDIRECT_URL )

#     return render(request, self.template_name)


# class LogoutView(TemplateView):

#   template_name = 'idcomplete/index.html'

#   def get(self, request, **kwargs):

#     logout(request)

#     return render(request, self.template_name)


# def register(response):
# 	if response.method == "POST":
# 		form = RegisterForm(response.POST)
# 		if form.is_valid():
# 			form.save()

# 		return redirect("/home")
# 	else:
# 		form = RegisterForm()

# 	return render(response, "register/register.html", {"form":form})



