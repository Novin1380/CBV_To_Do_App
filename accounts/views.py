from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect

# Create your views here.


class CustomLoginView(LoginView):
    '''
    a class based view for logging in 
    '''
    template_name = "accounts/login.html"
    fields = "username","password"
    redirect_authenticated_user = True

    def get_success_url(self):
        # you can write this part with reverse or redirect
        return reverse_lazy("ToDo:task_list")


class RegisterPage(FormView):
    '''
    a class based view for registration and signing up 
    '''
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("ToDo:task_list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("ToDo:task_list")
        return super(RegisterPage, self).get(*args, **kwargs)