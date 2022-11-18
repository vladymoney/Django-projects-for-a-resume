from django.forms import ModelForm
from django import forms

from cars_exam.cars.models import Car
from cars_exam.my_profile.models import Profile


class BaseProfileForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")


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
        self.__hide_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __hide_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()
            field.required = False
