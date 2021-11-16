from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Recipe
from .serializers import RecipeSerializer

# def delete(request,recipe_id):
#     recipe_id=int(recipe_id)
#     note=Recipe.objects.get(id=recipe_id)
#     note.delete()

@api_view(['GET','POST','DELETE'])
def api_recipe(request,recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_recipe_data = request.data
        recipe.title = new_recipe_data['title']
        recipe.save()

    if request.method == 'DELETE':
        recipe.delete()
        
    serialized_recipe = RecipeSerializer(recipe)
    return Response(serialized_recipe.data)


@api_view(['GET','POST'])
def api_all(request):
    all_recipes=Recipe.objects.all()

    if request.method == 'POST':
        new_recipe_data = request.data
        recipe=Recipe()
        recipe.title=new_recipe_data['title']
        recipe.save()

        all_recipes=Recipe.objects.all()
    serialized_recipe = RecipeSerializer(all_recipes,many=True)
    return Response(serialized_recipe.data)