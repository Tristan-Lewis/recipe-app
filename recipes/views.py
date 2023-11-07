from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'recipes/recipes_home.html')


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
   model = Recipe  # specify model
   template_name = 'recipes/main.html'  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
   model = Recipe  # specify model
   template_name = 'recipes/detail.html'  # specify template
