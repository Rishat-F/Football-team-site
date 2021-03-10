# Generated by Django 3.1.3 on 2021-01-23 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=3)),
                ('position', models.CharField(max_length=3)),
                ('games', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('passes', models.IntegerField()),
                ('pm', models.IntegerField()),
            ],
        ),
    ]
