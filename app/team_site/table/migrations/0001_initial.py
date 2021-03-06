# Generated by Django 3.1.3 on 2021-01-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('games', models.PositiveSmallIntegerField()),
                ('wins', models.PositiveSmallIntegerField()),
                ('draws', models.PositiveSmallIntegerField()),
                ('loses', models.PositiveSmallIntegerField()),
                ('goals_scored', models.PositiveSmallIntegerField()),
                ('goals_allowed', models.PositiveSmallIntegerField()),
                ('points', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
