# Generated by Django 3.1.3 on 2021-01-31 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcalendar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('team1', models.CharField(max_length=50)),
                ('team2', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=5)),
                ('stage', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
