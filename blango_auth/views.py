from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse_lazy

# Create your views here.
@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")

class MyRegistrationView(RegistrationView):
    def register(self, form): 
        new_user = form.save(commit=False) # Do not automatically log in the user when they register
        new_user.save() 
        return new_user
    
    def get_success_url(self, request):
        return reverse_lazy("blog-index") # this could be overridden to redirect to a different page