# Generated by Django 3.2.6 on 2021-08-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='content',
        ),
    ]
