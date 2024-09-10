from django.shortcuts import render

# Create your views here.
def create_category(request): 
    template_name = "category/create_category.html"
    context = {}
    return render(request, template_name, context)