# Generated by Django 4.1.2 on 2022-11-23 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_inscricao_options_alter_inscricao_minicursos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscricao',
            old_name='name',
            new_name='nome',
        ),
    ]
