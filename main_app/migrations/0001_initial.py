# Generated by Django 3.2.4 on 2021-08-20 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('releaseDate', models.IntegerField()),
            ],
        ),
    ]
