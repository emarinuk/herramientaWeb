# Generated by Django 4.2 on 2023-04-29 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_alter_publicacion_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='tipo',
            field=models.CharField(choices=[('Libro', 'Libro'), ('Artículo', 'Artículo')], default='Libro', max_length=8),
        ),
    ]
