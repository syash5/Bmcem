# Generated by Django 2.1 on 2019-04-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmcem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
