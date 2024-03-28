from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from collections import defaultdict

from recipes.models import Recipe
from utils.django_forms import add_attr


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

        add_attr(self.fields.get('description'), 'class', 'span-2')
        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')

    class Meta:
        model = Recipe
        fields = [
            'title',
            'category',
            'description',
            'preparation_time',
            'preparation_time_unit',
            'servings',
            'servings_unit',
            'preparation_steps',
            'cover',
        ]
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Porções', 'Porções'),
                    ('Pedaços', 'Pedaços'),
                    ('Gramas', 'Gramas'),
                    ('Quilos', 'Quilos'),
                    ('Litros', 'Litros'),
                )
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Segundos', 'Segundos'),
                    ('Minutos', 'Minutos'),
                    ('Horas', 'Horas'),
                    ('Dias', 'Dias'),
                )
            ),
        }

    def clean(self, *args, **kwargs) -> dict:
        super_clean = super().clean(*args, **kwargs)

        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        preparation_time = cleaned_data.get('preparation_time')
        servings = cleaned_data.get('servings')

        if len(title) < 5:
            self._my_errors['title'].append('Título deve ter mais de 5 caracteres!')

        if title == description:
            self._my_errors['title'].append('Título não pode ser igual a descrição!')
            self._my_errors['description'].append('Descrição não pode ser igual ao título!')

        if preparation_time <= 0:
            self._my_errors['preparation_time'].append('Tempo de preparo inválido!')

        if servings <= 0:
            self._my_errors['servings'].append('Quantidade inválida!')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean
