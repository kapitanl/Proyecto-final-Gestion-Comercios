# Generated by Django 3.1.7 on 2021-03-07 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionComerciosApp', '0010_comercioforms_comercio_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comercioforms',
            name='comercio_user',
        ),
    ]