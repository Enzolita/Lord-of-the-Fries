from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponse
# Create your views here.


class Index(View):
    template_name = "home/index.html"

def home_page(request):
    return HttpResponse("Hello, Home!")
    template_name = "home/index.html"
    paginate_by = 6

def recipe_view(request):
    return render(request, 'recipe.html')
 

