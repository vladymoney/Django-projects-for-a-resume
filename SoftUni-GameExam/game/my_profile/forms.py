from django.forms import ModelForm
from django import forms

from game.my_game.models import Game
from game.my_profile.models import Profile


class BaseProfileForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ("email", "age", "password")


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    password = forms.CharField(widget=None)

    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.required = False
