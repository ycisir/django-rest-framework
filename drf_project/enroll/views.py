from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .form import StudentRegistration
from .models import User
from django.contrib import messages
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


class UserAddShowView(TemplateView):
    template_name = 'enroll/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentRegistration()
        students = User.objects.all()
        context = {'students':students, 'form':form}
        return context
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            stud_name = fm.cleaned_data['name']
            stud_email = fm.cleaned_data['email']
            stud_pass = fm.cleaned_data['password']
            register = User(name=stud_name, email=stud_email, password=stud_pass)
            register.save()
            messages.success(request, 'Added successfully')
        
        return HttpResponseRedirect('/')


class UserUpdateView(View):
    def get(self, request, id):
        tmp = User.objects.get(pk=id)
        form = StudentRegistration(instance=tmp)
        return render(request, 'enroll/update.html', {'form':form})
    
    def post(self, request, id):
        tmp = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=tmp)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            messages.success(request, 'Updated successfully')
            
        return HttpResponseRedirect('/')



# this function will update and edit
# def update_student(request, id):
#     if request.method == 'POST':
#         tmp = User.objects.get(pk=id)
#         fm = StudentRegistration(request.POST, instance=tmp)
#         if fm.is_valid():
#             fm.save()
#             fm = StudentRegistration()
#             messages.success(request, 'Updated successfully')
#             return HttpResponseRedirect('/')




class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['id']
        User.objects.get(pk=delete_id).delete()
        return super().get_redirect_url(*args, **kwargs)

