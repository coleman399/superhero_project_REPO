from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    hero = Superhero.objects.get(pk = hero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheros/detail.html', context)

def create(request):
    if request.method == 'POST':
        #   save the form content as a new database object
        #   return to index
        print("Hit with POST")
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary_ability')
        secondary = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name = name, alter_ego = alter_ego, primary_ability = primary, secondary_ability = secondary, catch_phrase = catch_phrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def edit(request, hero_id):
    hero = Superhero.objects.get(pk = hero_id)
    if request.method == 'POST':
        edit_name = request.POST.get('name')
        edit_alter_ego = request.POST.get('alter_ego')
        edit_primary = request.POST.get('primary_ability')
        edit_secondary = request.POST.get('secondary_ability')
        edit_catch_phrase = request.POST.get('catch_phrase')
        new_hero = Superhero(name = edit_name, alter_ego = edit_alter_ego, primary_ability = edit_primary, secondary_ability = edit_secondary, catch_phrase = edit_catch_phrase)
        new_hero.save()
        Superhero.delete(hero)
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
            'hero': hero
        }
        return render(request, 'superheroes/edit.html', context)

def delete(request, hero_id):
    delete_superhero = Superhero.objects.get(pk=hero_id)
    Superhero.delete(delete_superhero)
    return HttpResponseRedirect(reverse('superheroes:index'))
