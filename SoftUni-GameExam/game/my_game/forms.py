from django.forms import ModelForm
from django import forms

from game.my_game.models import Game


class BaseGameForm(ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.required = False
