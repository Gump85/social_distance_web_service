from django import forms
from .models import UploadImage


class ImageUploadForm(forms.ModelForm):
    """ форма для сохранения объекта изображения в базе"""
    class Meta:
        model = UploadImage
        fields = ('image', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-group col-md-6'}),
            'description': forms.Textarea(attrs={'class': 'form-control col-md-8'}),
        }
