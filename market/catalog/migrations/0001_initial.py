# Generated by Django 4.1.5 on 2023-04-16 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfCountries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.listofcountries')),
            ],
        ),
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(default='tours/tours-tours-default.jpg', upload_to='tours/')),
                ('short_desc', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('availability', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('room_desc', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.listofcountries')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.regions')),
            ],
        ),
    ]
