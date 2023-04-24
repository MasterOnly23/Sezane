
from django import forms
from django import forms
from prendas.models import Prendas

SEARCH_OPTIONS = (('Prenda','Prenda'),
              ('Talla','Talla'),
              ('Color','Color'),
              ('Cantidad','Cantidad'),
              )


class Buscar(forms.Form):
    search_option = forms.ChoiceField(choices=SEARCH_OPTIONS)
    search_term = forms.CharField(max_length=100)





class Formulario(forms.ModelForm):

    class Meta:
        model = Prendas
        fields = '__all__'