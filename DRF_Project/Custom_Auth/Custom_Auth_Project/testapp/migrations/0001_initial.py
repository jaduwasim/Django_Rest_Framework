# Generated by Django 4.1.4 on 2023-06-27 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField()),
                ('ename', models.CharField(max_length=64)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]