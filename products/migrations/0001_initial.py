# Generated by Django 4.1.2 on 2024-02-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('desc', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=70)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
