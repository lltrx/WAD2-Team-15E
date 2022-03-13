from django import forms
#from rango.models import Page, Category, UserProfile
from rango.models import UserProfile, Destination, Place
from django.contrib.auth.models import User


class DestinationForm(forms.ModelForm):
    # Change name of vars and types
    name = forms.CharField(max_length=128,
                           help_text="Please enter the destination name.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.CharField(max_length=200, help_text="Please enter the description.")
    image = forms.ImageField(help_text="Select a destination image.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Destination
        fields = ('name', 'description', 'image')

    class Meta:
        model = Destination
        fields = ('name',)


class PlaceForm(forms.ModelForm):
    # Change name of var and the type this one is helpful for places
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the place.")
    address = forms.URLField(max_length=200,
                         help_text="Please enter the address of the place.")


    class Meta:
        model = Place
        exclude = ('destination',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('about', 'picture',)
        