# Generated by Django 4.1.2 on 2022-11-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('nascimento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=120)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('curso', models.CharField(choices=[('T', 'Curso técnico'), ('S', 'Curso superior'), ('E', 'Curso extra-curricular')], max_length=1)),
                ('minicursos', models.IntegerField(choices=[(1, 'Introdução a Computação Gráfica'), (2, 'Introduição a construção de jogos'), (4, 'Realidade Virtual'), (8, 'Computação nas Nuvens')])),
            ],
        ),
    ]