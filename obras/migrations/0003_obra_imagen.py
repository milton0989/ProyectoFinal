# Generated by Django 4.1.7 on 2023-03-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_remove_obra_imagen_alter_obra_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='obras'),
        ),
    ]