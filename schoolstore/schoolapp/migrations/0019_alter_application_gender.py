# Generated by Django 4.1.3 on 2023-06-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0018_alter_application_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
