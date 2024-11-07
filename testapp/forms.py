from django import forms
from django.core import validators

from testapp.models import Img


class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение',
                           validators=[validators.FileExtensionValidator(
                               allowed_extensions=('gif','jpg','png'))],
                           error_messages={
                               'invalid_extension':'Этот формат не поддерживается'})

    decs = forms.CharField(label = '', widget=forms.widgets.Textarea())

    class Meta:
        model = Img
        fields = '__all__'

