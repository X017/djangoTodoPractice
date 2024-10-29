from django.shortcuts import render
from .models import todo_list
# Create your views here.

def hello_world(request):
    my_list = todo_list.objects.all()
    return render(request,'home.html',{'my_list':my_list})
