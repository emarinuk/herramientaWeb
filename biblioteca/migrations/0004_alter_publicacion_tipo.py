# Generated by Django 4.2 on 2023-04-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_publicacion_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='tipo',
            field=models.CharField(choices=[('LI', 'Libro'), ('AR', 'Artículo')], default='Libro', max_length=8),
        ),
    ]
