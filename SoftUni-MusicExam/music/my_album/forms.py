from django.forms import ModelForm
from django import forms
from music.my_album.models import Album


class AlbumBaseForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "album_name": forms.TextInput(attrs={"placeholder": "Album Name"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
            "description": forms.Textarea(attrs={"placeholder": "Description"}),
            "image_url": forms.URLInput(attrs={"placeholder": "Image URL"}),
            "price": forms.TextInput(attrs={"placeholder": "Price"}),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteAlbum(AlbumBaseForm):
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
