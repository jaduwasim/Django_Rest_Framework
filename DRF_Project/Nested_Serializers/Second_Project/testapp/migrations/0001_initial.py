# Generated by Django 4.1.4 on 2023-06-25 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('instrument', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Musician',
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField()),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_musician', to='testapp.musician')),
            ],
            options={
                'db_table': 'Album',
            },
        ),
    ]