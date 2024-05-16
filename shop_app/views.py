from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.http import HttpResponse, HttpResponseNotFound
from .models import Tool, Category#, Parts



def index(request):
    cats = Category.objects.filter()
    tool = Tool.is_published.all()
    data = {
        'tool': tool,
        'cats': cats,
    }

    return render(request, 'index.html', context=data)

def list_tool(request, tool_slug):
    tool = get_object_or_404(Tool, slug=tool_slug)

    data = {
        'tool': tool,
    }

    return render(request, 'tool.html', data)

def list_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    tools = Tool.objects.filter(category=category)

    data = {
        'category': category.name,
        'tools': tools,
        'category_selected': category.pk,
    }

    return render(request, 'cat.html', data)


def sale(request):
    return render(request, 'sale_product.html')

def rent(request):
    cats = Category.objects.filter()

    data = {
        'cats': cats,
    }

    return render(request, 'rent_category.html', data)

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about.html')

def catalog(request):
    return render(request, 'catalog.html')

def payment(request):
    return render(request, 'payment.html')

def buying(request):
    return render(request, 'buying.html')

