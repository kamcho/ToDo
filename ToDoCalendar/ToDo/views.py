import random
import secrets

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, UpdateView, ListView, DetailView
from .models import Task

# Create your views here.


class TaskList(ListView):
    model = Task
    template_name = 'ToDo/tasks.html'
    context_object_name = 'tasks'


class CreateTask(TemplateView):
    template_name = 'ToDo/create.html'

    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            title=request.POST.get('title')
            about=request.POST.get('about')
            date=request.POST.get('date')
            task=Task.objects.create(title=title,reminder=date,about=about)

            task.save()

            return redirect('tasks')

class UpdateTask(DetailView):
    template_name = 'ToDo/details.html'
    model = Task
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            title=request.POST.get('title')
            about=request.POST.get('about')
            date=request.POST.get('date')
            # task=Task.objects.create(title=title,reminder=date,about=about)
            #
            # task.save()
            if "edit" in request.POST:
                task=Task.objects.get(id=self.kwargs['pk'])
                task.title=title
                task.about=about
                task.reminder=date
                task.save()
                return redirect(f'tasks')
            else:
                request.session['delete']=self.kwargs['pk']
                return redirect(f'delete')


            #
            # task.save()

            # return redirect('tasks')






class DeleteTask(TemplateView):
    template_name = 'ToDo/delete.html'
    code=""
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeleteTask, self).get_context_data(**kwargs)
        self.code=secrets.token_hex(4)
        context['code']=self.code
        self.request.session['code']=self.code
        return context
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            if "purge" in request.POST:
                delete=request.POST.get('delete')
                print(self.code)
                if delete == request.session['code']:
                    print("deleting\n\n\n")
                    task = Task.objects.get(id=request.session['delete']).delete()
                    print(task)
                    return redirect('tasks')
                else:
                    return redirect('tasks')




