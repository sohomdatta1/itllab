# Generated by Django 4.0.3 on 2022-04-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
    ]
