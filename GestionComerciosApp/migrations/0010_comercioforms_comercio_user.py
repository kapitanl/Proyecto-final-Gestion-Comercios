# Generated by Django 3.1.7 on 2021-03-06 23:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GestionComerciosApp', '0009_postdecomerciosforms_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercioforms',
            name='comercio_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
