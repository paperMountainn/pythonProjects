from django import forms
from django.http import request
from .models import First_app

class SampleForm(forms.ModelForm):
    # defining fields, if same name as those in Meta, can save in db
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Put your title here"}))
    description = forms.CharField(required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class": "description",
                                "id": "1234",
                                "rows":20,
                                "cols": 120,
                            }
                        ))
    price = forms.DecimalField(initial=19.999)

    # to illustrate validation, as you can see this is not saved into db, 
    # we didn't define an email field in the first place
    email = forms.EmailField()

    # for saving into DB
    class Meta:
        model = First_app
        fields =[
            "title",
            "description",
            "price"
        ]

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email.")
        return email


# Raw form
# looks like our model, which is supposed to be looking like it!
# instantiating form fields
class sampleDjangoForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Put your title here"}))
    description = forms.CharField(required=False, 
                        widget=forms.Textarea(
                            attrs={
                                "class": "description",
                                "id": "1234",
                                "rows":20,
                                "cols": 120,
                            }
                        ))
    price = forms.DecimalField(initial=19.999)
