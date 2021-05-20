from django.shortcuts import render
from django.http import HttpResponse
from .models import First_app
from .forms import SampleForm, sampleDjangoForm
# Create your views here.

# hardcoded views
def home_view(request, *args, **kwargs):
    my_context ={
        "greeting":"hello there!",
        "name": "My name is Zoe,",
        "about": "I am from SUTD",
        "stuffs_i_like": ["Code", "Cats", "Art", "mom"],
    }
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", my_context)

def contacts_view(request, *args, **kwargs):
    my_context = {
        "spirit_animal": "<p>Doge</p>",
        "name": "Zoe",
        "number": 123,
    }
    return render(request, "contacts.html", my_context )

# db views
def my_description_view(request):
    obj = First_app.objects.get(id=2)
    context = {
        "object": obj
    }
    return render(request, "myself/details.html", context)


def form_create_view(request):
    # intiial data, you can use any of the fields
    # initial_data =  {
    #     'title': "This is awesome title"
    # }
    # obj = First_app.objects.get(id=1)
    
    form = SampleForm(request.POST or None)
    if form.is_valid():
        form.save()
        
    context = {
        "form": form
    }
    return render(request, "sample_form.html", context)


def django_form_view(request):
    # print(request.POST)
    # print(request.GET)
    my_form = sampleDjangoForm()

    if request.method == "POST":
        my_form = sampleDjangoForm(request.POST)
        # check if form valid
        if my_form.is_valid():
            form_data = my_form.cleaned_data
            print(form_data)
            First_app.objects.create(**form_data)
            # print(form_dict['title'])
            # print(form_dict.get('title'))
        else:
            print(my_form.errors)

    # this form is parsed over to the html side to be rendered.
    context = {
        "form": my_form
    }
    return render(request, "django_form.html", context)