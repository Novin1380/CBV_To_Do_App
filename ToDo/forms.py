from django import forms
from .models import Task 



class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'id':'task-input', "name": "title", "placeholder": "Write the title",}),label="",)
    
    
    class Meta:
        model = Task
        fields = ("title",)