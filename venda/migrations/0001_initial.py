# Generated by Django 4.0.2 on 2022-02-08 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_ordem', models.DateTimeField(auto_now_add=True)),
                ('completada', models.BooleanField(default=False)),
                ('id_transacao', models.CharField(max_length=100, null=True)),
                ('consumidor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='venda.consumidor')),
            ],
        ),
        migrations.CreateModel(
            name='ItemOrdem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(blank=True, default=0, null=True)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('ordem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venda.ordem')),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venda.livro')),
            ],
        ),
        migrations.CreateModel(
            name='Enderecoenvio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=200)),
                ('data_adicionado', models.DateTimeField(auto_now_add=True)),
                ('consumidor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venda.consumidor')),
                ('ordem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='venda.ordem')),
            ],
        ),
    ]