from django.urls import path
from .views import home, search, RecipeListView, RecipeDetailView
app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('search/', search, name='search'),
    path('recipe-list/', RecipeListView.as_view(), name='list'),
    path('recipe/<pk>', RecipeDetailView.as_view(), name='detail'),
]
