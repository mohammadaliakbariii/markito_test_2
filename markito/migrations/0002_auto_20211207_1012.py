# Generated by Django 3.2.9 on 2021-12-07 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markito', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name_plural': 'channels'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'products'},
        ),
    ]