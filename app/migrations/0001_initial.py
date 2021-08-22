# Generated by Django 3.2.6 on 2021-08-07 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Pasta', 'Pasta'), ('Egg Dishes', 'Egg Dishes'), ('Fried Dishes', 'Fried Dishes'), ('Rice Dishes', 'Rice Dishes')], max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(blank=True, max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='app/image')),
            ],
        ),
    ]
