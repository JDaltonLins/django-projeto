from django.db import models

# Create your models here.


class Inscricao(models.Model):
    CURSO_CHOICES = (
        ('T', 'Curso técnico'),
        ('S', 'Curso superior'),
        ('E', 'Curso extra-curricular')
    )

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    MINICURSOS_CHOICES = (
        (1, 'Introdução a Computação Gráfica'),
        (2, 'Introduição a construção de jogos'),
        (4, 'Realidade Virtual'),
        (8, 'Computação nas Nuvens')
    )

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    nascimento = models.DateField()
    email = models.EmailField()
    endereco = models.CharField(max_length=120)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=1)
    curso = models.CharField(choices=CURSO_CHOICES, max_length=1)
    minicursos = models.IntegerField()

    def minicursos_items(self):
        return [item[1] for item in Inscricao.MINICURSOS_CHOICES if item[0] & self.minicursos]

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
