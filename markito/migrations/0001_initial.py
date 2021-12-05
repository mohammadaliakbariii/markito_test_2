# Generated by Django 3.2.9 on 2021-12-05 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField(default=0)),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('side_costs', models.DecimalField(decimal_places=2, max_digits=50)),
                ('costs', models.DecimalField(decimal_places=2, max_digits=50)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markito.categories')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]
