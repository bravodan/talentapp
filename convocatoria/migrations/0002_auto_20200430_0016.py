# Generated by Django 3.0.5 on 2020-04-30 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulacionanonima',
            name='full_name',
            field=models.CharField(max_length=120, verbose_name='Nombre completo'),
        ),
    ]
