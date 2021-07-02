# Generated by Django 3.2.4 on 2021-07-01 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
                ('last_modified', models.DateField(auto_now=True)),
            ],
        ),
    ]
