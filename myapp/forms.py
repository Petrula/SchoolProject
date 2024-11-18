from .models import People
from django.forms import ModelForm, TextInput, Select


class FormPeople(ModelForm):
    class Meta:
        model = People
        fields = ["name", "phone", "sport_section"]
        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя', }),
            "phone": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер', }),
            "sport_section": Select(attrs={'class': 'form-control', 'placeholder': 'Спортивная секция'},
                                           choices=[('box', 'Бокс'), ('wrestling', "Борьба"), ('wushu', "Ушу")]),
        }

