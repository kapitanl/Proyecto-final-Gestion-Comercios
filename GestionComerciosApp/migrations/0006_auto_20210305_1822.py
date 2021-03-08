# Generated by Django 3.1.7 on 2021-03-05 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionComerciosApp', '0005_productosforms'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categoria_productos', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='productosforms',
            name='categroia_pruductos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='GestionComerciosApp.categoriaproductos'),
        ),
    ]