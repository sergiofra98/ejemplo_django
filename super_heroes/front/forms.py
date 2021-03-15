from django.forms import ModelForm
from .models import SuperHeroe, SuperPoder

class HeroeForm(ModelForm):
    class Meta:
        model = SuperHeroe
        fields = '__all__'


class PoderForm(ModelForm):
    class Meta:
        model = SuperPoder
        fields = '__all__'