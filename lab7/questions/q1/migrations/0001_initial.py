# Generated by Django 2.2.28 on 2022-04-28 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('num_of_visits', models.IntegerField()),
                ('num_of_likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('views', models.IntegerField()),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='q1.Category')),
            ],
        ),
    ]
