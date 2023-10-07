from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

people = []  # List to store Person objects

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            people.append(person)
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'person_app/add.html', {'form': form})

def person_list(request):
    return render(request, 'person_app/list.html', {'people': people})
