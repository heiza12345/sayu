# Generated by Django 4.1.3 on 2023-06-26 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='age',
            field=models.IntegerField(),
        ),
    ]
