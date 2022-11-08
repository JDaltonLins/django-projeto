from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout


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


class CursoForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100,
                           widget=forms.TextInput(attrs={'form_style': 'inline'}))
    cpf = forms.CharField(label='CPF', max_length=14)
    nascimento = forms.DateField(label='Nascimento')
    email = forms.EmailField(label='Email')
    endereco = forms.CharField(label='Endereço', max_length=120)
    sexo = forms.ChoiceField(label='Sexo', choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ], widget=forms.RadioSelect)
    curso = forms.ChoiceField(label='Curso', choices=[
        ('T', 'Curso técnico'),
        ('S', 'Curso superior'),
        ('E', 'Curso extra-curricular')
    ])
    minicursos = forms.MultipleChoiceField(label='Minicursos', choices=[
        ('CG', 'Introdução a Computação Gráfica'),
        ('CJ', 'Introduição a construção de jogos'),
        ('RV', 'Realidade Virtual'),
        ('CN', 'Computação nas Nuvens')
    ], widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'name',
            'cpf',
            'email',
            'nascimento',
            'endereco',
            'sexo',
            'curso',
            'minicursos',
            Submit('submit', 'Enviar', css_class='btn btn-primary')
        )
