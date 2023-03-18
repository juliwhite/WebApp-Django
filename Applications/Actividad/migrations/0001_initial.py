# Generated by Django 4.1.7 on 2023-03-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30)),
                ('activities', models.CharField(max_length=60)),
                ('date', models.DateField()),
            ],
        ),
    ]