# Generated by Django 4.1.7 on 2023-03-30 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0006_alter_obra_autor_alter_obra_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
