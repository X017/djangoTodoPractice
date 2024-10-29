from django import forms
from .models import todo_list

class todoListForm(forms.Form):
    model = todo_list
    fields = ['title','body','finish']