from django import forms # Vou trabalhar com formulários
from .models import Sorvete

class SorveteForm(forms.ModelForm):
    class Meta:
        model = Sorvete
        fields = '__all__'