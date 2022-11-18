from django import forms
from django.forms import ModelForm

from music.my_album.models import Album
from music.my_profile.models import Profile


class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "age": forms.TextInput(attrs={"placeholder": "Age"}),
        }


class CreateProfileForm(ProfileBaseForm):
    pass


class DeleteProfileForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hide_fields()

    def save(self, commit=True):
        if commit:
            Album.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __hide_fields(self):
        for _, field in self.fields.items():
            field.required = False
            field.widget = forms.HiddenInput()
