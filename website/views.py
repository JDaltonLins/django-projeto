from django.shortcuts import render, redirect
from website.forms import CursoForm
from website.models import Inscricao


def index(request):
    return redirect('form/cadastrar')


def inscricoes(req):
    return render(req, 'inscricoes.html', {
        "page": {
            "title": "Inscrições",
        },
        "inscricoes": Inscricao.objects.all()
    })


def cadastro(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form/inscricoes')
    else:
        form = CursoForm()

    return render(request, 'cadastro.html', {
        "page": {
            "title": "Formulário de Inscrição",
        },
        "form": form
    })
