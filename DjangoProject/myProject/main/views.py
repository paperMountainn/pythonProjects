from django.shortcuts import render

# Create your views here.
# hardcoded views
def main_home_view(request, *args, **kwargs):
    my_context ={
        "greeting":"hello there!",
        "name": "My name is Zoe,",
        "about": "I am from SUTD",
        "stuffs_i_like": ["Code", "Cats", "Art", "mom"],
    }
    # return HttpResponse("<h1>Hello World</h1>")s
    return render(request, "home.html", my_context)

def main_contacts_view(request, *args, **kwargs):
    my_context = {
        "spirit_animal": "<p>Doge</p>",
        "name": "Zoe",
        "number": 123,
    }
    return render(request, "contacts.html", my_context )