# Generated by Django 4.0.4 on 2022-11-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_note_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['description']},
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(max_length=250, unique=True),
        ),
    ]