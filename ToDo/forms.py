from django import forms
from .models import Task 



class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded-4' , "name": "title", "placeholder": "Write the title",}),label="",)
    
    
    class Meta:
        model = Task
        fields = ("title",)