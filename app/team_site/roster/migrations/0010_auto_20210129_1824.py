# Generated by Django 3.1.3 on 2021-01-29 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0009_auto_20210129_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(choices=[('gk', 'вратарь'), ('un', 'полевой игрок')], max_length=2),
        ),
    ]
