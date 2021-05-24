from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import First_app
from .forms import SampleForm, sampleDjangoForm
# Create your views here.

# # hardcoded views
# def firstapp_home_view(request, *args, **kwargs):
#     my_context ={
#         "greeting":"hello there!",
#         "name": "My name is Zoe,",
#         "about": "I am from SUTD",
#         "stuffs_i_like": ["Code", "Cats", "Art", "mom"],
#     }
#     # return HttpResponse("<h1>Hello World</h1>")s
#     return render(request, "home.html", my_context)

# def firstapp_contacts_view(request, *args, **kwargs):
#     my_context = {
#         "spirit_animal": "<p>Doge</p>",
#         "name": "Zoe",
#         "number": 123,
#     }
#     return render(request, "contacts.html", my_context )

# db views
def firstapp_my_description_view(request):
    obj = First_app.objects.get(id=10)
    
    context = {
        "object": obj
    }
    return render(request, "details.html", context)

# db view, but rendered dynamically according to the id
def firstapp_my_decription_dynamic_view(request, my_id):
    obj = First_app.objects.get(id=my_id)
    # obj = get_object_or_404(First_app, id=my_id)

    context = {
        "object": obj
    }

    return render(request, "details.html", context)

def firstapp_descr_list_view(request):
    queryset = First_app.objects.all()

    context ={
        "objects": queryset
    }

    return render(request, "descr_list.html", context)



def firstapp_form_create_view(request):
    # intiial data, you can use any of the fields
    # initial_data =  {
    #     'title': "This is awesome title"
    # }
    
    # editing model form data 
    obj = First_app.objects.get(id=11)

    form = SampleForm(request.POST or None, instance=obj)
    if form.is_valid():
        print("form saved in db")
        form.save()
    else:
        print(form.errors)

    context = {
        "form": form
    }
    return render(request, "sample_form.html", context)


def firstapp_django_form_view(request):
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


def firstapp_delete_object_view(request, my_id):
    obj = get_object_or_404(First_app, id=my_id)

    if request.method == "POST":
        obj.delete()
        return redirect("../../")

    context = {
        "object": obj
    }

    return render(request, "delete_object.html", context)

