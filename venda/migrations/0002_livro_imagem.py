# Generated by Django 4.0.2 on 2022-02-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]