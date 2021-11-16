from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('api/recipes/<int:recipe_id>/', views.api_recipe),
    path('api/recipes/', views.api_all),
    # Você possivelmente tem outras rotas aqui.
]