from django.shortcuts import render
from app.models import *
from django.urls import reverse_lazy
from app.forms import *
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView,FormView

class Home(TemplateView):
    template_name='app/Home.html'


class School_list(ListView):
    model = School
    context_object_name='schools'


class School_Detail(DetailView):
    model=School
    context_object_name='schlobject'

class School_form(CreateView):
    model=School
    fields='__all__'


class Student_form(FormView):
    form_class=Studentform
    template_name='app/Student_form.html'
    success_url=reverse_lazy('Student_list')
    def form_valid(self,form):
        form.save()
        return HttpResponse('data inserted sucessfully')


class School_Update(UpdateView):
    model=School
    fields='__all__'

class School_Delete(DeleteView):
    model=School
    context_object_name='schlobject'
    success_url=reverse_lazy('School_list')