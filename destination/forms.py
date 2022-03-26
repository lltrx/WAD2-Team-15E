from django import forms
from destination.models import UserProfile, Destination
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

DESTINATION_TYPES = [('H', 'History'), ('S', 'Sport'), ('R', 'Relax'), ('O', 'Other')]

class DestinationForm(forms.ModelForm):
    # Change name of vars and types
    name = forms.CharField(max_length=128,
                           help_text="Please enter the destination name.")
    destination_type = forms.ChoiceField(choices=DESTINATION_TYPES)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    description = forms.CharField(max_length=300, help_text="Please enter the description.")
    image = forms.ImageField(help_text="Select a destination image.", required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Destination
        fields = ('name', 'destination_type', 'description', 'image')

    def save(self, request, commit=True):
        destination = super(DestinationForm, self).save(commit=False)
        destination.name = self.cleaned_data["name"]
        destination.destination_type = self.cleaned_data["destination_type"]
        destination.description = self.cleaned_data["description"]
        destination.image = self.cleaned_data["image"]
        destination.author = request.user
        if commit:
            destination.save()
        return destination


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
            )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "picture",
            "about"
            )
class UserProfileChangeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "picture",
            "about"
            )
        
class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password")