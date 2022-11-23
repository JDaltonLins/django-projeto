from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Div, Field

from website.models import Inscricao
from functools import reduce

"""
    Formulário contendo os seguintes campos
    Nome (Req|Str|Max:100)
    CPF (Req|Str|Formato:000.000.000-00)
    Nascimento (Req|Data)
    Email (Req|Str|Formato:<EMAIL>)
    Endereço (Req|Str|Max:120)
    Sexo (Req|Radio|Itens:Masculino;Feminino)
    Curso (Req|Dropbox|Itens:Curso técnico;Curso superior; Curso extra-curricular)
    Minicursos (Checkbox List|Itens:Introdução a Computação Gráfica;Introduição a construção de jogos;Realidade Virtual;Computação nas Nuvens)
"""


class CursoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100,
                           widget=forms.TextInput(attrs={'form_style': 'inline'}))
    cpf = forms.CharField(label='CPF', max_length=14)
    nascimento = forms.DateField(label='Nascimento')
    email = forms.EmailField(label='Email')
    endereco = forms.CharField(label='Endereço', max_length=120)
    sexo = forms.ChoiceField(
        label='Sexo', choices=Inscricao.SEXO_CHOICES, widget=forms.RadioSelect)
    curso = forms.ChoiceField(label='Curso', choices=Inscricao.CURSO_CHOICES)
    minicursos = forms.MultipleChoiceField(
        label='Minicursos', choices=Inscricao.MINICURSOS_CHOICES, widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'f d-flex flex-column'
        self.helper.form_style = 'inline'
        self.helper.form_group_wrapper_class = 'mb-1 d-flex flex-row'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(Field('nome', wrapper_class="w-100", css_class=""), Field('cpf',
                wrapper_class="w-100"), css_class='d-flex flex-row col'),
            'email',
            'nascimento',
            'endereco',
            'sexo',
            'curso',
            'minicursos',
            Submit('submit', 'Enviar', css_class='btn btn-primary align-self-end')
        )

        # Inicia o minicursos, transformando de Integer Bitwise para MultipleChioiceFIeld
        self.fields['minicursos'].initial = self._minicursos_to_choices(
            self.initial.get('minicursos', 0))

    def _minicursos_to_choices(self, minicursos):
        return [c for c in Inscricao.MINICURSOS_CHOICES if c[0] & minicursos]

    def _choices_to_minicursos(self, choices):
        return reduce(lambda x, y: x | y, [int(c[0]) for c in choices], 0)

    def save(self, *args, **kwargs):
        # Salva o minicursos, transformando de MultipleChioiceFIeld para Integer Bitwise
        self.cleaned_data['minicursos'] = self._choices_to_minicursos(
            self.cleaned_data['minicursos'])
        self.instance.minicursos = self.cleaned_data['minicursos']
        return super().save(*args, **kwargs)

    class Meta:
        fields = ['nome', 'cpf', 'nascimento', 'email',
                  'endereco', 'sexo', 'curso']
        model = Inscricao
