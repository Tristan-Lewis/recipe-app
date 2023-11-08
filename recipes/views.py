from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
from .models import Recipe
import pandas as pd
from .utils import get_chart


def home(request):
    return render(request, 'recipes/recipes_home.html')


def search(request):
    # create an instance of SalesSearchForm that you defined in sales/forms.py
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    chart = None

    # check if the button is clicked
    if request.method == 'POST':
        # read book_title and chart_type
        name = request.POST.get('name')
        chart_type = request.POST.get('chart_type')
        qs = Recipe.objects.filter(name=name)
        if qs:  # if data found
           # convert the queryset values to pandas dataframe
           recipes_df = pd.DataFrame(qs.values())
           chart = get_chart(chart_type, recipes_df,
                             labels=recipes_df['name'].values)
           recipes_df = recipes_df.to_html()
        # display in terminal - needed for debugging during development only
        print(name, chart_type)

    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart
    }

    # load the sales/record.html page using the data that you just prepared
    return render(request, 'recipes/search.html', context)


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/main.html'  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'
    # specify template
