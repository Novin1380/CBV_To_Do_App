from django.shortcuts import render,redirect
from django.db.models.query import QuerySet
from django.views.generic import DeleteView,UpdateView,CreateView,FormView,ListView,TemplateView,RedirectView,DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskUpdateForm
from django.views import View

# Create your views here.
# def IndexView(request):
#     return render(request,"ToDo/update_task.html")



class  TaskListView(LoginRequiredMixin,ListView):
    '''
    a class based view to show index page and first view list
    '''
    model = Task
    ordering = '-id'
    context_object_name = "tasks"
    template_name = "ToDo/list_task.html"
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    # queryset = Task.objects.all()

class DeleteView(LoginRequiredMixin, DeleteView):
    '''
    a class based view to delete items from list
    '''
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("ToDo:task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    

class TaskCreate(LoginRequiredMixin, CreateView):
    '''
    a class based view to create items by clicking on add button
    '''
    model = Task
    ordering = '-id'
    fields = ["title"]
    success_url = reverse_lazy("ToDo:task_list")

    def form_valid(self, form):
        try:
            form.instance.user = self.request.user
        except:
            redirect("ToDo:task_list")
        return super(TaskCreate, self).form_valid(form)
    
        
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    '''
    a class based view to edit and update items
    '''
    model = Task
    ordering = '-id'
    success_url = reverse_lazy("ToDo:task_list")
    form_class = TaskUpdateForm
    template_name = "todo/update_task.html"
    

    
    
class TaskComplete(LoginRequiredMixin, View):
    '''
    a class based view to make the items Done!
    '''
    model = Task
    ordering = '-id'
    success_url = reverse_lazy("ToDo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.done = True
        object.save()
        return redirect(self.success_url)
    
class TaskUndo(LoginRequiredMixin, View):
    model = Task
    ordering = '-id'
    success_url = reverse_lazy("ToDo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.done = False
        object.save()
        return redirect(self.success_url)
    
