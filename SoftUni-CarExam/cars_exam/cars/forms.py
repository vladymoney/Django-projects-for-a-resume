from django.forms import ModelForm

from cars_exam.cars.models import Car


class BaseCarForm(ModelForm):
    class Meta:
        model = Car
        fields = ["type", "model", "year", "image_url", "price"]


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
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
