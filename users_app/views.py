from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.views import LogoutView

from .forms import CustomRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created! Login to Get Started"))
            return redirect('register')
    else:
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

#