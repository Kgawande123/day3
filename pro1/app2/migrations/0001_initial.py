# Generated by Django 5.0.6 on 2024-06-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator1',
            fields=[
                ('num1', models.IntegerField(primary_key=True, serialize=False)),
                ('num2', models.IntegerField()),
                ('choice', models.CharField(max_length=32)),
            ],
        ),
    ]
