from django.shortcuts import render
from website.forms.CursoForm import CursoForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def curso_form(request):
    form = CursoForm()
    helper = form.helper
    helper.form_class = 'form-horizontal'

    helper.label_class = 'col-lg-2'
    helper.field_class = 'col-lg-8'

    return render(request, 'curso_form.html', {
        "page": {
            "title": "Formulário de Inscrição",
        },
        "form": form
    })
