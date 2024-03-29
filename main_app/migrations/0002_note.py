# Generated by Django 4.0.4 on 2022-11-08 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('content', models.TextField(max_length=250)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.skill')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
