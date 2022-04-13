from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import FacultySignupForm, ParentSignupForm, StudentSignupForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail

def index(request):
    return render(request, 'user/index.html')

class FacultySignupView(CreateView):
    model = User
    form_class = FacultySignupForm
    template_name = 'registration/signup_faculty.html'

  
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'faculty'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')   

class StudentSignupView(CreateView):
    model= User
    form_class = StudentSignupForm
    template_name = 'registration/signup_student.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        return redirect('/')  

class ParentSignupView(CreateView):
    model= User
    form_class = ParentSignupForm
    template_name = 'registration/signup_parent.html'
    success_url ="/user/index/"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')  

class MultiLoginView(LoginView):

    template_name = 'user/multilogin.html'
    success_url ="/user/index/"

    def get(self, request, *args, **kwargs):
       print(self.request.user)
       return self.render_to_response(self.get_context_data())

def sendmail(request):
    subject = 'welcome'
    message = 'hello world!!!'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['fenil.g.shah.2001@gmail.com', 'priteshptadvi29@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return HttpResponse("mail sent..")
