# Generated by Django 3.1.7 on 2021-04-09 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estoque', '0004_auto_20210402_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['-id'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
    ]
