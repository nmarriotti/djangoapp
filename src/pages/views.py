from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "title": "Sample Django App"
    }
    return render(request, "home.html", my_context)