# Generated by Django 3.1.7 on 2021-03-06 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionComerciosApp', '0007_auto_20210305_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaproductos',
            name='pertenece',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GestionComerciosApp.postdecomerciosforms'),
            preserve_default=False,
        ),
    ]
