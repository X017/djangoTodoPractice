# Generated by Django 5.1.2 on 2024-10-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_list',
            name='finish',
            field=models.BooleanField(),
        ),
    ]