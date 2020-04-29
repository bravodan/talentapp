# Generated by Django 3.0.5 on 2020-04-29 04:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulacionanonima',
            name='apply_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de postulación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postulacionanonima',
            name='convocatoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='convocatoria.Convocatoria', verbose_name='convocatoria'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postulacionanonima',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha y hora de última actualización'),
        ),
    ]