# Generated by Django 3.1.7 on 2021-04-05 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_vendas', '0004_venda_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descrição da Venda'),
        ),
    ]