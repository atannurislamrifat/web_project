# Generated by Django 5.0.3 on 2024-03-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('f_name', models.CharField(max_length=10)),
                ('l_name', models.CharField(max_length=10)),
                ('number', models.IntegerField()),
                ('mail', models.CharField(max_length=10)),
                ('msg', models.CharField(max_length=10)),
            ],
        ),
    ]